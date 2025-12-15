import sys
from .coxkan.CoxKAN import CoxKAN
from .coxkan import datasets, utils

# Register nested modules in sys.modules for external imports
sys.modules['coxkan.datasets'] = datasets
sys.modules['coxkan.utils'] = utils

__all__ = ['CoxKAN', 'datasets', 'utils']
