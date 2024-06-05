import streamlit as st

st.set_page_config(page_title='INFORMASI PRODUK TAHU PUTRA TASIK')
st.image('PUTRA TASIK (1).jpg')
tab1,tab2,tab3,tab4=st.tabs(['Proses Pembuatan Produk','Penyimpanan Tahu','Cara Pemesanan','Informasi Harga'])

with tab1:
    st.video('Pembuatan tahu vidio.MP4')
    
with tab2:    
    st.write('Masa penyimpanan tahu tergantung bagaimana cara menyimpannya. Berikut tata cara menyimpan tahu agar tahan lama dan tidak asam ala Tahu Putra Tasik')
    st.image('Menu Poster Makanan (1).jpg')
  
with tab3:
    st.write('Untuk memesan Tahu Putra Tasik, Putra Tasik Tahu Lovers dapat langsung mendatangi pabrik tahu dan jika ingin delivery order, Putra Tasik Tahu Lovers dapat menghubungi nomor atau email yang tertera')
    st.image('3.jpg')
    
with tab4:
    st.image('1.jpg')