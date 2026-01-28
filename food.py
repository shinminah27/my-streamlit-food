import streamlit as st
import random
import time
import urllib.parse

# 1️⃣ 페이지 설정
st.set_page_config(page_title="메뉴 추천기", page_icon="🍱")

# 2️⃣ 카테고리별 메뉴 데이터
menu_data = {
    "한식": ["제육볶음", "김치찌개", "비빔밥", "불고기 백반", "뼈해장국", "부대찌개", "순두부찌개"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "볶음밥", "꿔바로우", "잡채밥"],
    "일식": ["돈카츠", "연어덮밥", "라멘", "가츠동", "소바", "텐동"],
    "양식": ["치즈버거", "까르보나라", "페퍼로니 피자", "스테이크 샐러드", "오므라이스", "샌드위치"],
    "분식/기타": ["떡볶이", "모둠 튀김", "잔치국수", "샐러드볼", "편의점 정식", "토스트"],
    "간식": ["붕어빵🐟", "호떡", "아이스크림🍦", "바게트🥖", "도넛🍩"]
}

# 3️⃣ 메인 화면 구성
st.title("🍴 오늘 뭐 먹지?")
st.subheader(" AI가 골라주는 오늘의 메뉴")
st.markdown("---")

# 4️⃣ 사이드바: 카테고리 선택
with st.sidebar:
    st.header("⚙️ 옵션 설정")
    category = st.selectbox("음식 종류를 선택하세요", ["전체"] + list(menu_data.keys()))
    st.info("카테고리를 선택하지 않으면 '전체' 메뉴에서 무작위로 추천합니다.")

# 5️⃣ 메뉴 추천 버튼
if st.button("🚀 메뉴 추천받기"):
    # 카테고리에 따라 메뉴 리스트 생성
    if category == "전체":
        all_menus = []
        for menus in menu_data.values():
            all_menus.extend(menus)
        final_list = all_menus
    else:
        final_list = menu_data[category]

    # 로딩 스피너
    with st.spinner("오늘의 완벽한 메뉴를 찾는 중..."):
        time.sleep(1.5)
        result = random.choice(final_list)

    # 결과 표시
    st.success("오늘의 추천 메뉴는 바로...!")
    st.markdown(f"<h1 style='text-align:center; color:#E74C3C;'>{result}</h1>", unsafe_allow_html=True)

    # 🎈 풍선 효과
    st.balloons()

    # 🍱 랜덤 음식 이미지 (Unsplash + 대체용 Picsum)
    query = urllib.parse.quote(result)  # 한글 URL 인코딩
    image_url = f"https://source.unsplash.com/600x400/?{query},food"
    fallback_url = f"https://picsum.photos/600/400"

    # 이미지 표시 (예외 대비)
    try:
        st.image(image_url, caption=f"{result} (랜덤 이미지)", use_container_width=True)
    except:
        st.image(fallback_url, caption="랜덤 이미지", use_container_width=True)

    # 🎉 애니메이션 텍스트
    st.markdown("""
    <div style='text-align:center; font-size:40px; animation: pop 1s ease infinite;'>
      🎉 맛있겠다! 🎉
    </div>
    <style>
    @keyframes pop {
      0% { transform: scale(1); }
      50% { transform: scale(1.2); }
      100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

# 6️⃣ 오늘의 운세 문구
st.markdown("---")
fun_quotes = [
    "고민은 배송만 늦출 뿐, 배고픔만 더할 뿐입니다!",
    "맛있게 먹으면 0칼로리라는 말을 믿으세요.",
    "오늘 먹을 메뉴를 내일로 미루지 마세요.",
    "다 먹고 살자고 하는 공부입니다. 든든하게 드세요!"
]
st.caption(f"💡 {random.choice(fun_quotes)}")

