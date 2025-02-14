# local
import ivy_tests.test_ivy.helpers as helpers
from ivy_tests.test_ivy.helpers import handle_frontend_method


# argmax
@handle_frontend_method(
    method_tree="numpy.matrix.argmax",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("numeric"),
        min_num_dims=2,
        max_num_dims=2,
        min_dim_size=2,
        valid_axis=True,
        force_int_axis=True,
        allow_neg_axes=False,
    ),
)
def test_numpy_matrix_argmax(
    dtype_x_axis,
    as_variable,
    native_array,
    class_,
    method_name,
):
    input_dtype, x, axis = dtype_x_axis
    if isinstance(axis, tuple):
        axis = axis[0]
    helpers.test_frontend_method(
        init_input_dtypes=input_dtype,
        init_as_variable_flags=as_variable,
        init_num_positional_args=0,
        init_native_array_flags=native_array,
        init_all_as_kwargs_np={
            "data": x[0],
            "dtype": input_dtype[0],
        },
        method_input_dtypes=[],
        method_as_variable_flags=as_variable,
        method_num_positional_args=0,
        method_native_array_flags=native_array,
        method_all_as_kwargs_np={
            "axis": axis,
        },
        frontend="numpy",
        class_="matrix",
        method_name="argmax",
    )


# any
@handle_frontend_method(
    method_tree="numpy.matrix.any",
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("numeric"),
        min_num_dims=2,
        max_num_dims=2,
        min_dim_size=2,
        valid_axis=True,
        force_int_axis=True,
        allow_neg_axes=False,
    ),
)
def test_numpy_matrix_any(
    dtype_x_axis,
    as_variable,
    native_array,
    class_,
    method_name,
):
    input_dtype, x, axis = dtype_x_axis
    if isinstance(axis, tuple):
        axis = axis[0]
    helpers.test_frontend_method(
        init_input_dtypes=input_dtype,
        init_as_variable_flags=as_variable,
        init_num_positional_args=0,
        init_native_array_flags=native_array,
        init_all_as_kwargs_np={
            "data": x[0],
            "dtype": input_dtype[0],
        },
        method_input_dtypes=[],
        method_as_variable_flags=as_variable,
        method_num_positional_args=0,
        method_native_array_flags=native_array,
        method_all_as_kwargs_np={
            "axis": axis,
        },
        frontend="numpy",
        class_="matrix",
        method_name="any",
    )


# transpose
@handle_cmd_line_args
@given(
    dtype_x_axis=helpers.dtype_values_axis(
        available_dtypes=helpers.get_dtypes("numeric"),
        min_num_dims=2,
        max_num_dims=2,
        min_dim_size=2,
    ),
)
def test_numpy_transpose(
    dtype_x_axis,
    as_variable,
    native_array,
    fw,
):
    input_dtype, x, axis = dtype_x_axis
    helpers.test_frontend_method(
        input_dtypes_init=input_dtype,
        as_variable_flags_init=as_variable,
        num_positional_args_init=0,
        native_array_flags_init=native_array,
        all_as_kwargs_np_init={
            "data": x[0],
            "dtype": input_dtype[0],
        },
        input_dtypes_method=[],
        as_variable_flags_method=as_variable,
        all_as_kwargs_np_method={
            "axis": axis,
        },
        num_positional_args_method=0,
        native_array_flags_method=native_array,
        fw=fw,
        frontend="numpy",
        class_name="matrix",
        method_name="transpose",
    )
