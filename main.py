
import streamlit as st
from PIL import Image
import io
import style




st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Pytorch Style Transfer")

img = st.sidebar.selectbox(
    'Select an Image',
    ('amber.jpg', 'Dog.jpg')
)


style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic','rain_princess','udnie')
)



model = "saved_models/" + style_name + ".pth"
input_images = "images/content-images/" + img
output_image = "images/output-images/" + style_name + "-" + img


st.write("### Source Image:")
image = Image.open(input_images)
st.image(image, width = 400)

cliked = st.button("Stylize")
if cliked:
    model = style.load_model(model)
    style.stylize(model, input_images, output_image)

    st.write("### Outut Image:")
    image = Image.open(output_image)
    st.image(image, width = 400)



uploaded_file = st.sidebar.file_uploader("Choose an Image", type="jpg")
st.write("### Your Image:")
print(type(uploaded_file))
if uploaded_file:
    image_test = Image.open(uploaded_file)
    st.image(image_test, width = 400)

cliked = st.button("Stylize your image")
if cliked:
    model = style.load_model(model)
    style.stylize(model, uploaded_file, output_image)

    st.write("### Transformed Image:")
    image = Image.open(output_image)
    st.image(image, width = 400)