import streamlit as st
from Views.AddPostView import AddPostView
from Views.FeedView import FeedView
from Services.AddPost import add_post
from Services.GetFeed import get_feed
from pages.page_1 import func_page_1
from pages.page_2 import func_page_2

st.title("Social Network")

AddPostView(add_post)
st.write("___")
FeedView(get_feed)

def main():
    st.sidebar.subheader('Page selection')
    page_selection = st.sidebar.selectbox('Please select a page',['Main Page',
    'Page 1','Page 2'])
    pages_main = {
        'Main Page': main_page,
        'Page 1': run_page_1,
        'Page 2': run_page_2
    }

    # Run selected page
    pages_main[page_selection]()

def main_page():
    st.title('Main Page')
def run_page_1():
    func_page_1()
def run_page_2():
    func_page_2()
if __name__ == '__main__':
    main()