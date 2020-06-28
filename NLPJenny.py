import streamlit as st



def main():
## Title and description

	st.title('NLPJenny')
	st.subheader("Natural Language Processing On the Go..")
	st.markdown("""
			#### Description
			+ This is a Natural Language Processing(NLP) Based App useful for basic NLP task
			implemented using State of he Art API's on Streamlit Framework.
			""")
	### features


	




	#SIDE BAR

	st.sidebar.header("About App")
	st.sidebar.subheader("NLPJenny")
	st.sidebar.text("Natural Language Processing On the Go")


	st.sidebar.subheader("Contact Developer")
	st.sidebar.text("Aryan Chaudhary")
	st.sidebar.text("aryanc55@gmail.com")
	st.sidebar.markdown("""  [Github](https://github/aryanc55)""")

	
	st.sidebar.markdown("[![Build Status](https://img.shields.io/travis/markdown-it/markdown-it/master.svg?style=flat)](https://travis-ci.org/markdown-it/markdown-it)")
	
if __name__ == "__main__":
	main()