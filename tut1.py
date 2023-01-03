import streamlit as st

st.title("Welcome to Streamlit Tutorials !")
st.header("Tut-1 Learning Some Text Elements")
st.markdown('''
- Title -> Main Title
- Header -> For a Heading
- Subheader -> For Sub-headings
- Text -> For witing plain texts and paragraphs
- Markdown -> For various markdown options (h1-h6 tags, codeblock, horizontal rule, table, images, etc)
- Caption ->  To write captions
- Latex -> To wrote mathematical formulaes and equations
- JSON -> To write JSON codes
- Code -> To write codes
- 
''')
st.markdown('---')
st.header("This is a Header")
st.subheader("This is our subheader.")
st.text("This is text function. Used to write texts.")

st.markdown('---')
st.markdown("**Hello** *World !*")
# h1 tag
st.markdown("# This is h1 tag")
# blockquote
st.markdown("> This is blockquote")


# Code
st.markdown("This is a code block")
st.markdown('''
```
import pandas as pd
df = pd.read_csv("abc.csv)
print(df.head())
```
''')

# Links
st.text("Links in Markdown")
st.markdown('[Google](https://www.google.com/)')
st.markdown('[Markdown Guide](https://www.markdownguide.org/cheat-sheet/)')
st.markdown('---')

# Captions
st.caption("Hi! I'm a Caption.")

# Latex
st.text("This is Latex")
st.text("A Matrix")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
st.markdown("[Latex Guide](https://katex.org/docs/supported.html)")


st.markdown('---')
# JSON
st.text('JSON Format')
json_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
st.json(json_data)

#Codes
st.text('CODE Formats')
code_data = '''
# Hello World Code
print('Hello World')
def func():
    return 0
'''
st.code(code_data, language='python')

code_data = '''
# Hello World Code
int main(){
cout<<"Hello World";
return 0;
}
'''
st.code(code_data, language='cpp')