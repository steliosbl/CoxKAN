import sys
from .coxkan.CoxKAN import CoxKAN
from .coxkan import datasets, utils
from .coxkan import hyperparam_search

# Register nested modules in sys.modules for external imports
sys.modules['coxkan.datasets'] = datasets
sys.modules['coxkan.utils'] = utils
sys.modules['coxkan.hyperparam_search'] = hyperparam_search

__all__ = ['CoxKAN', 'datasets', 'utils', 'hyperparam_search']
