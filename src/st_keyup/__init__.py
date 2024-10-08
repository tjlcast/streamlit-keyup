from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called st_keyup,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"st_keyup", path=str(frontend_dir)
)

# Create the python function that will be called
def st_keyup(
    label: str,
    value: Optional[str] = "",
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        label = label,
        value = value,
        key=key,
        default=value,
    )

    return component_value


def demo():
    st.write("## Example")
    value = st_keyup("This is a demo")
    st.write(value)

    st.write("## Example with value")
    value2 = st_keyup("With a default value!", value="Default value")
    st.write(value2)


if __name__ == "__main__":
    demo()
