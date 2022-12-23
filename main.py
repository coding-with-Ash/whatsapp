import pywhatkit
import streamlit as st
import webbrowser as web
import time, webbrowser, pyautogui

## pip install pywhatkit
## if u get any flask related errors
    ## pip uninstall Flask Jinja2
    ## pip install Flask Jinja2


################################################### Defining Static Data ###############################################
st.sidebar.image('https://i.flockusercontent2.com/q884s08qs8s9s4lb?r=1157408321',
                 use_column_width=False)
st.sidebar.markdown("<marquee >By **Ashish Gopal**</marquee>", unsafe_allow_html=True)

user_color      = '#000000'
title_webapp    = "Whatsapp Webapp"

html_temp = f"""
            <div style="background-color:{user_color};padding:12px">
            <h1 style="color:white;text-align:center;">{title_webapp}
            <img src = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw0NDQ0NDQ0NDQ0NDw0NDw0NDQ8NDRANFRYXFhURFRUYHSggGBolGxUVITIhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGhAQFy0mICUtKy0tLS0tLSstKysrKysrLS0tLSstKy0tLS0tLSstKy0rLSsrLS0rLSstLS8tLS0rLf/AABEIAOEA4QMBIgACEQEDEQH/xAAbAAEBAAIDAQAAAAAAAAAAAAAAAQIGBAUHA//EAD0QAAICAQEEBwUFBwMFAAAAAAABAhEDBAUGITESQVFhcYGREyOhscEUMkJS0SJDYnKS4fBTgvEzY6Kjwv/EABsBAQADAQEBAQAAAAAAAAAAAAABBAUGAwIH/8QANxEAAgEBBAgDBwMEAwAAAAAAAAECAwQRITEFEkFRYXGBkSKhsRMjMkLB0eEGcvAUJGLxUqKy/9oADAMBAAIRAxEAPwDZwAYR+eAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGNggBBbFkABbFkABbBAAWxZAAUWQAFsWQAFsWQAFFkABbBAAWxZAAWxZAAWwQAFsWQAGVgxABAQAFBAAUEABQQAFBBYBQSz76bS5crrFjlP+VNL1JSvJScncle+GLPiDuMG7Oql99Qx9zlGT+Byo7pz69Ql4Y2/qeqoVH8pcjo21yV6pPrcvVo10GyPdOXVqf/X/AHPhl3Xzr7uSM16S9OQdnqr5SXoy1rOm+6fozogcvU7M1GHjkwtL80afxRw7PJprBlOcJQd0k09zVz8yggIPkoIACggAKCAAoIACghQDAEAIKCAAoIACggAKcvZ+zs2plWONpfem+CXi/ojn7C2DLPWXLccX4Uuc/DsNyxYowioQSjFcFFci1Rszn4pYI2LBomVdKpUwjs3v7Ljnu3nU7P3dwYujLJ73Iut/swT7o9fnZ3MYqKSSSS5JKkj46rU48MenklGEe19b7Eutmva3evmsGO/45v5R/Vl3WpUVdkb0qtksMdXCPBYt/Xq+5tJG650jz3PtnVZL6WeST6lUF8KOFKTfNyfi2zwdtWyP88zOqafgvgpt82l6ax6enfIp5cuHK14No5WHaWogqhmnDu5xIVtW2PmRDT8X8VJ9Hf6pHo51mu2Np89uUKl+eDalff1M6DRb1ZY0s0I5b/HF9B/KmbHs/aeHUr3c+K5xknGS/XxR7xq0qqu8maNK2WW2R1MH/jJY/bs2altTYebTXJe8xr94klS711fI6o9RNZ23u6p3l08anzljXJ96vkytWst2MOxk27QzgtehitsdvTfyz4vI1QET6vKnzsFIwCggAKCAAoIAC2CWAALMbFggyFmNiwDIhLFgkys7jd3ZH2iftMi9xB8vzvs8DrNBpZajLDFDnJtJ/ljz+CPRtNp4YoRxwVRgqX6lqzUdd3vJGvomwKvP2k14Y+bz7LN9OKPrFJJJKkuCS4JI6nbe2YaVdFVPM1ahdJLvf0MtvbVWlxcKeWdqEXy75PuRoWScpScpNylJ3KTfFvtZYtFo1PDHP0NTSmk/Ye6p/Ftf/H8s+2r1eTPPp5Zucu/gkuyupHyMVbaSTbfBJK234HKybPzwTlLDOMVxbceCXaZzveJy105tyxe9592cewY2LIPgpbMbFgkyEZNNSi3FrimnTT7mY2LBBtmxN4um44tS0pPhHLyUn2NdTNoPKza91tsOVabM7lVY5vnJK7T+hfs9pberPozpNF6UcmqNZ8n9H9H0Z9N59jqaeoxR94uM0vxLl0l3o1Kz1I0TebZvsMvTgqx5LkuyLX3l9fM+bVRu8a6nxpmwKP8AcQWHzffq8Hxue1s6ghLFlI58ysGNiwQZWDGxYBkDGyAAEABQQAFIAk20lzbil4vkA3cbhuZoujinnfPK2o/ypu35v5Gw5ckYQc5uowTk32JczDS4VixwxrlCKXj2s6XfLVqGnjhvjmfH+WNNmurqNLl6nbJRsNj/AGrvL8yZq209bLU5p5Jcm6S/LFdX+drOLZicnZmJZM+KD5Smk/DrRk4yZxj16s8XfKT83+TcN29kRwY1lmvfTVtvnFO6S7HXM74A2oQUI6qO+oUY0IKnDJfy/mzznbmj+z6nJBKo2pQfc1fw4nANu300nSxw1C/dNxk/4XVfX1NQMmtDUm0cXpCz+wtEoLLNcn9sV0KCA8ikUEABQm7TTaaaaa5prkyAA9F2Jr/tOnhkdKXGM0uqS/VU/Mu2dH9o0+TGvvNdKP8AMuXry8zVtz9X7PUSwt8M64dnSgpNfD6G8mtSkqtPHkztLDWVssvvMc4y/nFO/qeUop2G8Om9jq8qSqEmpR8GrZ1xlSTi2mcdUpunNwlmm12wKCAg+CggAKCAAxstmABBnYswBIMrOw3fx9PW6ePNdNv+mLkdad3uer1kO5Tf/i19T6pq+aXFFixx1rRTj/lH1Rv5oe+Ofp6tw6sUYr+pJv5o3w813hleu1D/AIor0VfQv2x+BLidJp6bVniltkvRv1uODZ99BqPY5seX8k1fgufwOMDOvOUjJxd6zR6yn6FOi3V2h7fTqEn7zClGXb0X91+nDyO9NqE1NKS2n6DQrRrU41I5PH8dMjUd7trKvsuNpu08klyi1Uox8bpmq2cvbOhlptRKErcbuEn+JdT+a8jhGTWnKU25HEW6vVq15OqrmsLt12z87c8mZWWzAHkVDOxZgCQZWWzAEA5Gi1HscuPInXQknfcqv4HqR5JLl5r5nqmkd4sT7YRfwResT+Jcjo/0/N+8h+1+v4NU36h7zTz/ADRyL+mn/wDRrNm3b9QuGB9jyL16Jp54WlXVWZulo6tsnxuf/VGdizAHiZxnZLMQQDKwYgAgICSCggAKd1uhkrXQX5lk+EWdIc/YWb2er083wSl0X4NUfVN3TT4liyT1LRTlulHter/I9NPNd441rtQu+L9Vf1PSjQ99cChqlkr/AKsFJvtcUk/gkX7YvBfxOm09BuzKW6S9GvVo6AEBnHInN2Vr5aXNDKuK5Sj+aL6v87EekabPDNCOTG+lCStM8rO73Z239mn7PI28E3z5+zfau4s2atqO55M2dE6QVCXs6j8L8n9nt772bXtzZcdZi6PCOSPGE31Psfiee58U8U5Y8kXCcXTi+LPVYSTSaaaatNO012nXbX2Th1camqmvu5EuK7n2ruLVez+08Uc/U19J6M/qPeU8J+UufHc+j4ebg7HaexdTpW3KDljXLLGpKu9dRzN2NivUTWbKvcQfJ/vJd3nz9DPVOTlq3YnMQslaVZUdVqXHYt/Jb+2Z0T+fHl1A9R1ejxZodDJjU41ST4NeDXFeRq2090pK56V9NdWJtRfq+D8z2qWWccViaFp0LXpK+D1lwwfbG/o7+Bq4LlxyhJxnGUJRdONO0/AhWMfLBkm+D8Ueq6WPRx449ahFeiR5ns3AsuoxYmr6c+i/J/8AJ6mXrEvifI6T9PQfvJ/tXa9/VGqb+TqOnj2vK/RL9TTzZd+8t5cMP9OE5Pxf/BrJXtLvqsy9LS1rZU6LtFFBAeJnFBAAUEABjYsgALYsgALZW2uK4NVT7zEEEPHA9U2dqlnwY8y/HG/B3Ul5NM6nfLRe103tIq54Xa/klSl9PQ4O4+0P2Z6WT+7+3j8OuP182bXOCknGSTTVNPk0+aNaLValz9TuKUo2+x4/Mrnwl/vFdDyWxZytraRafUZsCfSWNpJ/wtKk++nXkcQymrnczipxcJOMs02nzWZbFkAPk73YG8M9NWPJc8Dfnj713Wb1pdVjzQWTFNSg+tfLufceUHI0OuzaeXTw5HB9dLpRa7K5MsUbS4YSxRsWDS87OlTqLWj5rlvXB9Hkj1clGpbP3xi6Wox9H/uY3a84815Nmw6TaWnzJPFlhLuupf0viaEK0J5M6az26hXwpzT4ZPs/XLic0GMmkrbSrrfBGv7Y3nw4E44WsuXlwvoxfbdcfI+pzjBXyZ6V69OhHWqu5efRbehru9+dS1s0v3fRT8eimzpbLPJKcpSk3KUm5SbXFt8Wy4ccskowgnKc2opLhbfMxpS1pN7zg69V1qsql3xNu7m8FzyRsm5Gi6WaeeS4YklB/wAUlT9OJvBwNk7PjpsMMMePRVyl2yfX/nYcfeTaH2bTTkn7yf7EO2+t+StmpTiqNPHmzsbJSjYbJ49icpc/9XJckaRt3V+21WXIncX0VH+VKl8r8zr7IgZTbbvZxU6jnJzlm233d5bFkAPktiyAAtggAICWLBBQSxYBQSxYBsm42LpaqU/9PH8Xw+Vm+mo7g4KhqMnVN40vK7+aNm1mX2eLLkX4ISl5pNmnZro0r3zO10PH2dji3tvfm/okeY7Uz+11GbJ1TyNrwvh8KOKYx+rLZmZ4nFuTm3J5vHviUGN+Poy2D5TTyKCWLBJQ/wDOJLFgPEdFd/qyks+ul02TNNY8UJZJv8MVXm+xd7F24iMMborF7tp8zet19hvTxWfKvfSXCD/Auu+9/D1Ppu/u5HTVkzdGefnGuUPDtNiNCz2fVetPPcdXovRLpNVq3xbFu4vjw2cdmMpJJttJJW2+CS7TzfeTav2vO3H/AKWO1DvXW/8AO47bezb6knpsEr4pZJJ8G+DUV3dvoalZ5WqtreCOW0qaZ0gqj9hTeCze9rZyW3jyKCWLKhgFBLFgFBLFgFsEsAGNlIACggBBQQjYB6LuTj6Ogxy/PKcvR9H6HN25gy5tLlxYa6c+glbSSXSV35WfTY+L2elwR5NQi2u98X8Wc414Q92o8Dv6FD+1jRb+RJ3Z5XM0zTbku7zaj/bCDr1v6Ha6fdTQwpvE8jX55S+SZ3ObJGC6U5KC7ZSSXqzrNVvLosXB5lJ9kIyn8Vw+J8eyo087upX/AKGwWZeOMV+53/8Aps50NFhjFxWHGoyVOKiuK7+06LaG52nyJvDKWCXY7yQ9G+BcW+WklPoyWSEOrJJWvNK2d9ptViyx6WKcci7Yu68ewn3VVXYM+7rFbVqLVld3XLJroaDq909bjf7EVlXbGcY/B8TgT2PrI/e0+Rf7W16pUeqg83Y47GylPQFnbvjKS7P6X92eUx2Vqny0+R+EZM5en3Z12Rr3LhF/inOKr/bdnpYIVijvZEf0/RT8U5Psvoadodyop3qMvSX5IRpeb/sbPotFiwR6GLHHHHrptt97b4vzPtknGCcpNRiucpOkvM6Lae9elw3HG/b5F+GLcY+cq/U9lGlRxy9S9GjY7BHWwjxeb73voux3uTJGEXKUlGMVblJ0ku1s0vePefpqWHTNxhyll5OS7rXBd50u1dtajVv3k+jBO1iX7MV/fxOuKda1OXhjgvMw7fpmVVOnRvS2va+W5efIqBAVTBKCAAoIACksAElBCAgAxsWAZAxsWAZBmNiwDbM2++XgsemjCkl+1KWV/BI6rU7ya7J+/lFdkIxgvVcTqLFnpKtOWcmXKukLVV+Ko+mHpcZ5Jub6UpSlJ9dtv1ZDGxZ5lO7aZFxylFqUXJSXKUW015owsWAdvpt5ddj4e3lJdk4wl8XxOwhvrqlzxwl3tfozWLFn2qs1lJluFvtUFdGrLvf6m0PfbU/6WJeT/U4WferXz4LNGC/hhFfFpnSWLJdWo/mZM9IWqaudWXR3elx99VqsuV3lnLI+12/mfIxsWeZUbbd7d7MgY2LBBkDGxYBkDGxYBkDGxYBkDGxYBkDGwAYggBBQQAFBAAUEABQQAFBAAUEABQQAFBAAUEABQQAFBAAUEABQQAFBAASxZiADKxZiADKwYgAysWYgAysWYgAysWYgAysWYgAyFmIAMrFmIAMrFmIAMrFmIAMrBiADKxZiADKxZiADIGIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/Z"
            align="right" width=130px ></h1>
            </div>
            """
st.markdown(html_temp, unsafe_allow_html=True)
#########################
st.sidebar.header("About")
st.sidebar.info("This webapp gives a demo of Integration between 'Streamlit' and 'Whatsapp for Web' to send Automated whatsapp messages")

################################################### Defining Function ##############################################
def main():
    col1, col2 = st.columns(2)

    # to_phne =  '+918096158712'
    to_phne = col1.text_input('Enter Phone No. to send message to',
                              value='+918096158712',
                              help='Enter Phone Number with Country Code',placeholder='+918888888888')

    repeat_msg_count = col2.number_input('How Many times to repeat the message?', min_value=1, max_value=1000, value=1)


    # text_msg = 'Hello Ji'
    text_msg = st.text_area('Enter Message to Send!',
                            value='Hey there!',
                            placeholder='Enter Message to send')

    tab1, tab2 = st.tabs(['Send Now', 'Schedule to send later'])

    #############################################################
    with tab1:
        flag_open = st.checkbox('Send Message', value=False)

        if flag_open == True:
            text_msg_all = ''
            for i in range(repeat_msg_count):
                text_msg_all = text_msg_all + text_msg + '\n'


            pywhatkit.sendwhatmsg_instantly(phone_no = to_phne,
                                            message = text_msg_all,
                                            wait_time=10
                                            )

            time.sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            pyautogui.press('enter')
            flag_open = False

            pyautogui.hotkey('ctrl', 'r')

    with tab2:
        time_send = st.time_input('Time when to send the message')

        flag_open = st.checkbox('Send Schedule Message', value=False)

        if flag_open == True:
            text_msg_all = ''
            for i in range(repeat_msg_count):
                text_msg_all = text_msg_all + text_msg + '\n'

            pywhatkit.sendwhatmsg(  phone_no  = to_phne,
                                    message   = text_msg_all,
                                    time_hour = int(str(time_send).split(':')[0]),
                                    time_min  = int(str(time_send).split(':')[1]),
                                    wait_time=10,
                                    )

            time.sleep(5)
            pyautogui.hotkey('ctrl', 'w')
            pyautogui.press('enter')
            flag_open = False

            pyautogui.hotkey('ctrl', 'r')

if __name__ == "__main__":
    main()
#############################################################
