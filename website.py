import streamlit as st


if 'page' not in st.session_state:
  st.session_state['page'] = 'home'
if 'feature' not in st.session_state:
  st.session_state['feature'] = 'timing'


main_pages = ["home", "get started"]

st.set_page_config(page_title="Applicator.ai")

st.sidebar.header("Applicator.ai")
st.sidebar.markdown("***")
st.sidebar.write("")

for page in main_pages:        
  if page == st.session_state['page']:
    if st.sidebar.button(page.title(),type="primary"):
      st.session_state['page'] = page
      st.experimental_rerun()
  else:
    if st.sidebar.button(page.title(),type="secondary"):
      st.session_state['page'] = page
      st.experimental_rerun()

st.sidebar.markdown("***")
st.sidebar.write("")    

st.sidebar.markdown("[Join Discord](https://discord.gg/VZy9xPhaW2) | [See Code](https://github.com/peter942/applicator_ai)")



if st.session_state['page'] == 'home':

  header1, header2 = st.columns(2)
  with header1:
    st.header("An open-source tool for creating, optimising, and monitoring ChatGPT API Prompts")
    st.write("We believe that combining dozens or hundreds of prompts will be the key to achieving extraordinary things with AI - but to do this, getting individual prompts performing reliably is key.")
    st.write("Applicator is designed by builders for builders - to help developers rapidly build test, monitor and implement ChatGPT API queries.")
    if st.button("Get Started", key="get_started_1"):
      st.session_state['page'] = 'get started'
      st.experimental_rerun()
    st.markdown("[Join Discord](https://discord.gg/VZy9xPhaW2)")
  with header2:
    st.image("https://i.ibb.co/bzt5BZ2/3568060768-A-puppeteer-sitting-above-a-stage-holding-up-hundreds-of-puppets-red-curtain-strings-ever.png",use_column_width='always')

  st.markdown("***")


elif st.session_state['page'] == "get started":
    st.markdown("## Get started with version 0.05:")
    st.warning("Note: Currently, Applicator runs locally so you'll need to download the code, install the dependencies and run it locally. In this state, I don't think it'll be usable for most people but I'm sharing a guide just in case. If you struggle at any stage, I'd suggest you ask ChatGPT first or message in the Discord.")
    st.markdown("### 1) Test it out")
    st.markdown("The live version won't run queries, or save files, but you can test it out here [here](https://peter942-applicator-ai-applicator-hcb851.streamlit.app/)")
    st.markdown("### 2) Download the code")
    st.markdown("You can download the code from [here](https://github.com/peter942/applicator_ai)")
    st.markdown("### 3) Install the dependencies")
    st.markdown("You'll need to install the dependencies listed in the requirements.txt file. You can do this by running the following command in the terminal:")
    st.markdown("```pip install -r requirements.txt```")
    st.markdown("### Set your OpenAI local environment variables")
    st.markdown("You'll need to set your OpenAI API key as an environment variable. You can do this by running the following command in the terminal:")
    st.markdown("```export OPENAI_API_KEY=YOUR_API_KEY```")
    st.markdown("### 4) Run the code")
    st.markdown("You can run the code by running the following command in the terminal:")
    st.markdown("```streamlit run applicator.py```")
    st.markdown("### 5) Use the app")
    st.markdown("This should open the app in your browser. You can then use the app as normal - new prompts will save to prompts.csv file.")
    st.markdown("### 6) Implement prompts into code")
    st.markdown("When you save a prompt, the JSON will pop up - this is a hamhanded way to ensure that your prompt matches what's in the code.  You can copy and paste this into the code like for Python:")
    st.code("input_prompt = **PASTE IN PROMPT JSON HERE** \n\ninput_prompt.append({'role': 'user', 'content': '{}'.format(prompt)}")
    st.markdown("This will be done in a nicer way in the future!")
    
    
    
    
    
