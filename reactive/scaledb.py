from charmhelpers.core import hookenv
from charms.reactive import when
from charms.reactive import when_not
from charms.reactive import set_state


# Starting condition
@when_not('scaledb.downloaded')
def download_scaledb():
    # Do some work here to download the binary for architecture.
    # get configuration values, key to get the package.
    # scaledb-key
    set_state('scaledb.downloaded')

# Middle condition
@when('scaledb.downloaded', 'config-changed.scaledb-key')
def key_changed():
    remove_state('scaledb.downloaded')

@when('scaledb.downloaded')
@when_not('scaledb.configured')
def config_scaledb():
    # edit the config files, jina templates
    config = hookenv.config()
    theme = config['theme']
    set_state('scaledb.configured')

# End condidition

