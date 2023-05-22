import uuid

from redis import ConnectionPool, Redis, StrictRedis

from app.config import defaults


class Leaderboard(object):

    def __init__(self, leaderboard_id=None, **options):
        """Initialize a connection to a specific leaderboard. By default, will
        use a redis connection pool for any unique host:port:db pairing.

        The options and their default values (if any) are:

        host : the host to connect to if creating a new handle ('localhost')
        port : the port to connect to if creating a new handle (6379)
        db : the redis database to connect to if creating a new handle (0)
        page_size : the default number of items to return in each page (25)
        order : order to use when sorting the leaderboard members
        connection : an existing redis handle if re-using for this leaderboard
        connection_pool : redis connection pool to use if creating a new handle
        """
        self.id = leaderboard_id or uuid.uuid4()
        self.page_size = options.pop('page_size', defaults.page_size)
        self.order = options.pop('order', defaults.order)
        redis_connection = options.pop('redis_connection', None)
        if redis_connection:
            # allow the developer to pass a raw redis connection and
            # we will use it directly instead of creating a new one
            self.redis_connection = redis_connection
        else:
            connection = options.pop('connection', None)
            if isinstance(connection, (StrictRedis, Redis)):
                options['connection_pool'] = connection.connection_pool
            if 'connection_pool' not in options:
                options['connection_pool'] = Leaderboard.pool(
                    options.pop('host', defaults.redis_host),
                    options.pop('port', defaults.redis_port),
                    options.pop('db', defaults.redis_db),
                    options.pop('pools', defaults.pools),
                    **options
                )
            self.redis_connection = Redis(**options)

    @staticmethod
    def pool(host, port, db, pools={}, **options):
        """Fetch a redis connection pool for the unique combination of host
        and port. Will create a new one if there isn't one already.
        """
        key = (host, port, db)
        rval = pools.get(key)
        if not isinstance(rval, ConnectionPool):
            rval = ConnectionPool(host=host, port=port, db=db, **options)
            pools[key] = rval
        return rval
