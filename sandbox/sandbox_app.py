import streamlit as st
import SessionState
import time

""" Some streamlit notes (0.69.2)
"""


st.header("Expected Distributions of Bandits")


""" configure sidebar
"""
# st.sidebar.subheader("Select Options")
# prediction = st.sidebar.selectbox(
#     "Model", options=["Image Similarity", 'Color Similarity']
# )
# td_no = st.sidebar.number_input(
#     min_value=1, max_value=10, value=1, label="No"
# )
# go = st.sidebar.button("GO")
# slider_options = st.select_slider(1,10)


#counter = 0
#if go & (prediction == "Image Similarity"):
# if go:
#     counter += 1
#     st.subheader('works like a charm')
#     st.text(str(counter))

# inital_parameters = {
#     "mu": 0,
#     "sigma": 1
# }


"""
For each button, slider etc., it runs the py file again
st is working on solution to keep variables in enviroment
11/11 --> use SessionState workaround
"""

# ss = SessionState.get(mu=0)
# time.sleep(1)
# ss.x +=1
# st.text(str(ss.x))

""" Use st.empty to replace some content
"""

# with st.empty():
#     for seconds in range(60):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")

""" Note: st.empty() is a single container
"""

# with st.empty() as st_e:
#     for seconds in range(60):
#         st_e.text("Distribution looks as follows:")
#         chart_data = pd.DataFrame(
#         np.random.randn(20, 3), columns=['a', 'b', 'c'])
#         st_e.line_chart(chart_data)
#         st_e.text("This overwrites the line chart =/")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")


""" I want to refresh the app not when clicking but for every second
"""

# # Solution?:
#
# iteration = 0
# chart_data = pd.DataFrame(
#         np.random.randn(20, 3), columns=['a', 'b', 'c'])
#
# st.text(f"We observe iteration {iteration}")
# st.line_chart(chart_data)
#
# for _ in range(60):
#
#     chart_data = pd.DataFrame(
#     np.random.randn(20, 3), columns=['a', 'b', 'c'])
#     iteration +=1
#     time.sleep(1)

""" Declare two empty container and overwrite them for every second --> no need for with
"""

# fig1 = st.empty()
# fig2 = st.empty()
# st.line_chart(chart_data)
#
# for second in range(60):
#
#     fig1.write(str(second))
#     fig2.write(str(second/60))
#     time.sleep(1)