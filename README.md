# streamlit-keyup

A streamlit component that allows you to get input from a textbox after every key press

## Installation instructions 

```sh
pip install streamlit-keyup
```

## Usage instructions

```python
import streamlit as st

from st_keyup import st_keyup

value = st_keyup()

st.write(value)
