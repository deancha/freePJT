def message(domain, uidb64, token):
    return f"아래 링크를 클릭클릭 인증완료.\n\n회원가입 링크: http://{domain}/account/avtivate/{uidb64}/{token}\n\n안될거같네"