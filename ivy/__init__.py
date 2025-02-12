# class placeholders


class Container:
    pass


class NativeArray:
    pass


class NativeVariable:
    pass


class Array:
    pass


class Variable:
    pass


class Framework:
    pass


class Device:
    pass


class Node:
    pass


class Dtype:
    pass


array_significant_figures_stack = list()
array_decimal_values_stack = list()


# global constants
_MIN_DENOMINATOR = 1e-12
_MIN_BASE = 1e-5


# local
from .array import Array, Variable, add_ivy_array_instance_methods
from .array.conversions import *
from .container import (
    ContainerBase,
    Container,
    MultiDevContainer,
    add_ivy_container_instance_methods,
)
from .framework_handler import (
    current_framework,
    get_framework,
    set_framework,
    unset_framework,
    framework_stack,
    choose_random_framework,
    try_import_ivy_jax,
    try_import_ivy_tf,
    try_import_ivy_torch,
    try_import_ivy_mxnet,
    try_import_ivy_numpy,
    clear_framework_stack,
)
from . import framework_handler, func_wrapper
from .debugger import (
    set_debug_mode,
    set_breakpoint_debug_mode,
    set_exception_debug_mode,
    unset_debug_mode,
    debug_mode,
    debug_mode_val,
)
from . import debugger
from . import functional
from .functional import *
from . import stateful
from .stateful import *
from . import verbosity
from .inspection import fn_array_spec, add_array_specs

add_array_specs()

# add instance methods to Ivy Array and Container
from ivy.functional.ivy import (
    activations,
    creation,
    data_type,
    device,
    elementwise,
    general,
    gradients,
    image,
    layers,
    linear_algebra,
    losses,
    manipulation,
    norms,
    random,
    searching,
    set,
    sorting,
    statistical,
    utility,
)

add_ivy_array_instance_methods(
    Array,
    [
        activations,
        creation,
        data_type,
        device,
        elementwise,
        general,
        gradients,
        image,
        layers,
        linear_algebra,
        losses,
        manipulation,
        norms,
        random,
        searching,
        set,
        sorting,
        statistical,
        utility,
    ],
)

add_ivy_container_instance_methods(
    Container,
    [
        activations,
        creation,
        data_type,
        device,
        elementwise,
        general,
        gradients,
        image,
        layers,
        linear_algebra,
        losses,
        manipulation,
        norms,
        random,
        searching,
        set,
        sorting,
        statistical,
        utility,
    ],
)


class StaticContainer(ContainerBase):
    pass


add_ivy_container_instance_methods(
    StaticContainer,
    [
        activations,
        creation,
        data_type,
        device,
        elementwise,
        general,
        gradients,
        image,
        layers,
        linear_algebra,
        losses,
        manipulation,
        norms,
        random,
        searching,
        set,
        sorting,
        statistical,
        utility,
    ],
)

# data types
int8 = "int8"
int16 = "int16"
int32 = "int32"
int64 = "int64"
uint8 = "uint8"
uint16 = "uint16"
uint32 = "uint32"
uint64 = "uint64"
bfloat16 = "bfloat16"
float16 = "float16"
float32 = "float32"
float64 = "float64"
# noinspection PyShadowingBuiltins
bool = "bool"
nan = float("nan")
inf = float("inf")

valid_dtypes = (
    int8,
    int16,
    int32,
    int64,
    uint8,
    uint16,
    uint32,
    uint64,
    bfloat16,
    float16,
    float32,
    float64,
    bool,
)
valid_numeric_dtypes = (
    int8,
    int16,
    int32,
    int64,
    uint8,
    uint16,
    uint32,
    uint64,
    bfloat16,
    float16,
    float32,
    float64,
)
valid_int_dtypes = (int8, int16, int32, int64, uint8, uint16, uint32, uint64)
valid_float_dtypes = (bfloat16, float16, float32, float64)

# all
all_dtype_strs = (
    "int8",
    "int16",
    "int32",
    "int64",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "bfloat16",
    "float16",
    "float32",
    "float64",
    "bool",
)
numeric_dtype_strs = (
    "int8",
    "int16",
    "int32",
    "int64",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "bfloat16",
    "float16",
    "float32",
    "float64",
)
int_dtype_strs = (
    "int8",
    "int16",
    "int32",
    "int64",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
)
float_dtype_strs = ("bfloat16", "float16", "float32", "float64")

# valid
valid_dtype_strs = all_dtype_strs
valid_numeric_dtype_strs = numeric_dtype_strs
valid_int_dtype_strs = int_dtype_strs
valid_float_dtype_strs = float_dtype_strs

# invalid
invalid_dtype_strs = ()
invalid_numeric_dtype_strs = ()
invalid_int_dtype_strs = ()
invalid_float_dtype_strs = ()

promotion_table = {
    (int8, int8): int8,
    (int8, int16): int16,
    (int8, int32): int32,
    (int8, int64): int64,
    (int16, int8): int16,
    (int16, int16): int16,
    (int16, int32): int32,
    (int16, int64): int64,
    (int32, int8): int32,
    (int32, int16): int32,
    (int32, int32): int32,
    (int32, int64): int64,
    (int64, int8): int64,
    (int64, int16): int64,
    (int64, int32): int64,
    (int64, int64): int64,
    (uint8, uint8): uint8,
    (uint8, uint16): uint16,
    (uint8, uint32): uint32,
    (uint8, uint64): uint64,
    (uint16, uint8): uint16,
    (uint16, uint16): uint16,
    (uint16, uint32): uint32,
    (uint16, uint64): uint64,
    (uint32, uint8): uint32,
    (uint32, uint16): uint32,
    (uint32, uint32): uint32,
    (uint32, uint64): uint64,
    (uint64, uint8): uint64,
    (uint64, uint16): uint64,
    (uint64, uint32): uint64,
    (uint64, uint64): uint64,
    (int8, uint8): int16,
    (int8, uint16): int32,
    (int8, uint32): int64,
    (int16, uint8): int16,
    (int16, uint16): int32,
    (int16, uint32): int64,
    (int32, uint8): int32,
    (int32, uint16): int32,
    (int32, uint32): int64,
    (int64, uint8): int64,
    (int64, uint16): int64,
    (int64, uint32): int64,
    (uint8, int8): int16,
    (uint16, int8): int32,
    (uint32, int8): int64,
    (uint8, int16): int16,
    (uint16, int16): int32,
    (uint32, int16): int64,
    (uint8, int32): int32,
    (uint16, int32): int32,
    (uint32, int32): int64,
    (uint8, int64): int64,
    (uint16, int64): int64,
    (uint32, int64): int64,
    (float32, float32): float32,
    (float32, float64): float64,
    (float64, float32): float64,
    (float64, float64): float64,
    (bool, bool): bool,
}

backend = "none"

if "IVY_BACKEND" in os.environ:
    ivy.set_framework(os.environ["IVY_BACKEND"])

# Array Significant Figures #


def _assert_array_significant_figures_formatting(sig_figs):
    assert isinstance(sig_figs, int)
    assert sig_figs > 0


def _sf(x, sig_fig=3):
    if isinstance(x, np.bool_):
        return x
    f = float(np.format_float_positional(
        x, precision=sig_fig, unique=False, fractional=False, trim='k'
    ))
    if np.issubdtype(type(x), np.uint) :
        f = np.uint(f)
    if np.issubdtype(type(x), np.int) :
        f = np.int(f)
    x = f
    return x


vec_sig_fig = np.vectorize(_sf)
vec_sig_fig.__name__ = 'vec_sig_fig'


def array_significant_figures(sig_figs=None):
    """Summary.

    Parameters
    ----------
    sig_figs
        optional int, number of significant figures to be shown when printing

    Returns
    -------
    ret

    """
    if ivy.exists(sig_figs):
        _assert_array_significant_figures_formatting(sig_figs)
        return sig_figs
    global array_significant_figures_stack
    if not array_significant_figures_stack:
        ret = 3 
    else:
        ret = array_significant_figures_stack[-1]
    return ret


def set_array_significant_figures(sig_figs):
    """Summary.

    Parameters
    ----------
    sig_figs
        optional int, number of significant figures to be shown when printing

    """
    _assert_array_significant_figures_formatting(sig_figs)
    global array_significant_figures_stack
    array_significant_figures_stack.append(sig_figs)


def unset_array_significant_figures():
    """"""
    global array_significant_figures_stack
    if array_significant_figures_stack:
        array_significant_figures_stack.pop(-1)

# Decimal Values #


def _assert_array_decimal_values_formatting(dec_vals):
    assert isinstance(dec_vals, int)
    assert dec_vals >= 0


def array_decimal_values(dec_vals=None):
    """Summary.

    Parameters
    ----------
    dec_vals
        optional int, number of decimal values to be shown when printing

    Returns
    -------
    ret

    """
    if ivy.exists(dec_vals):
        _assert_array_decimal_values_formatting(dec_vals)
        return dec_vals
    global array_decimal_values_stack
    if not array_decimal_values_stack:
        ret = None
    else:
        ret = array_decimal_values_stack[-1]
    return ret


def set_array_decimal_values(dec_vals):
    """Summary.

    Parameters
    ----------
    dec_vals
        optional int, number of significant figures to be shown when printing

    """
    _assert_array_decimal_values_formatting(dec_vals)
    global array_decimal_values_stack
    array_decimal_values_stack.append(dec_vals)


def unset_array_decimal_values():
    """"""
    global array_decimal_values_stack
    if array_decimal_values_stack:
        array_decimal_values_stack.pop(-1)
