import math
import subprocess
import sys
from pathlib import Path

import streamlit as st


def launch_streamlit_when_opened_directly():
    """Run this app without requiring the user to type a Streamlit command."""
    try:
        running_in_streamlit = st.runtime.exists()
    except AttributeError:
        # Compatibility with older Streamlit releases.
        from streamlit.runtime.scriptrunner import get_script_run_ctx

        running_in_streamlit = get_script_run_ctx() is not None

    if __name__ == "__main__" and not running_in_streamlit:
        app_path = str(Path(__file__).resolve())
        try:
            subprocess.run(
                [sys.executable, "-m", "streamlit", "run", app_path],
                check=True,
            )
        except KeyboardInterrupt:
            pass
        except subprocess.CalledProcessError as error:
            raise SystemExit(
                "アプリを起動できませんでした。Streamlitがインストールされているか確認してください。"
            ) from error
        raise SystemExit


launch_streamlit_when_opened_directly()

st.set_page_config(page_title="そくわんしょうの けんしん", page_icon="🩺", layout="wide")

st.markdown("""
<style>
.stApp{background:#f4f9ff}.block-container{max-width:1180px;padding-top:.8rem}
.hero{padding:24px 28px;border-radius:24px;background:linear-gradient(135deg,#1769c2,#33a7d8);color:white;margin-bottom:20px;box-shadow:0 8px 24px rgba(23,105,194,.18)}
.hero h1{margin:0;font-size:2.35rem;line-height:1.35}.hero p{margin:10px 0 0;font-size:1.3rem;line-height:1.65}
.card{background:white;border:2px solid #dbeaf7;border-radius:20px;padding:20px 22px;margin:12px 0;box-shadow:0 5px 16px rgba(53,92,125,.07);font-size:1.18rem;line-height:1.8}
.card h3{font-size:1.45rem;margin-top:0}.notice,.good{padding:18px 20px;border-radius:15px;margin:14px 0;font-size:1.16rem;line-height:1.8}
.notice{background:#fff7da;border-left:8px solid #f4b942}.good{background:#e8f8ef;border-left:8px solid #35a66f}
.stButton button{min-height:58px;font-size:1.25rem;border-radius:16px}[data-testid="stSidebar"]{min-width:285px}
[data-testid="stSidebar"] label,.stRadio label,.stCheckbox label,.stSlider label,.stToggle label{font-size:1.12rem!important}
div[data-testid="stAlert"]{font-size:1.1rem}@media(max-width:700px){.hero h1{font-size:1.85rem}.hero p{font-size:1.12rem}.card{font-size:1.08rem}}
</style>
""", unsafe_allow_html=True)

def hero(title, subtitle):
    st.markdown(f'<div class="hero"><h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)

def back_figure(asymmetry, show_points):
    left_y = 103 if asymmetry else 94
    right_y = 85 if asymmetry else 94
    spine_mid = 166 if asymmetry else 180
    visibility = "visible" if show_points else "hidden"
    return f"""
    <svg viewBox="0 0 360 430" width="100%" style="max-height:430px">
      <rect x="12" y="8" width="336" height="410" rx="24" fill="#eef8ff"/><ellipse cx="180" cy="393" rx="105" ry="12" fill="#d6e8f5"/>
      <circle cx="180" cy="50" r="34" fill="#ffd9b8" stroke="#35536c" stroke-width="4"/><path d="M150 43 Q180 8 212 43 L208 29 Q180 2 152 29Z" fill="#39495a"/>
      <path d="M124 {left_y} Q180 77 236 {right_y} L230 272 Q180 294 130 272Z" fill="white" stroke="#35536c" stroke-width="4"/>
      <path d="M180 102 Q{spine_mid} 174 180 265" fill="none" stroke="#7aa7c7" stroke-width="6" stroke-linecap="round"/>
      <path d="M126 108 Q96 170 104 254M234 108 Q264 170 256 254" fill="none" stroke="#ffd9b8" stroke-width="24" stroke-linecap="round"/>
      <path d="M150 278 L139 381M210 278 L221 381" stroke="#284b70" stroke-width="32" stroke-linecap="round"/>
      <g visibility="{visibility}" fill="#ff6f61" stroke="white" stroke-width="4"><circle cx="126" cy="{left_y}" r="10"/><circle cx="234" cy="{right_y}" r="10"/><circle cx="150" cy="160" r="10"/><circle cx="210" cy="160" r="10"/><circle cx="145" cy="235" r="10"/><circle cx="215" cy="235" r="10"/></g>
      <text x="180" y="414" text-anchor="middle" font-size="18" fill="#35536c">うしろから みた え</text>
    </svg>"""

def forward_bend_figure(angle):
    """あしを うごかさず、こしを ちゅうしんに じょうはんしんを たおす よこむきの え。"""
    hip_x, hip_y = 235, 250
    rad = math.radians(angle)
    shoulder_x = hip_x - 120 * math.sin(rad)
    shoulder_y = hip_y - 120 * math.cos(rad)
    head_x = shoulder_x - 43 * math.sin(rad)
    head_y = shoulder_y - 43 * math.cos(rad)
    arm_x = shoulder_x - 7
    hand_y = min(354, shoulder_y + 118)
    words = "まえに かがめたよ" if angle >= 75 else "ゆっくり まえへ"
    return f"""
    <svg viewBox="0 0 460 430" width="100%" style="max-height:430px">
      <rect x="10" y="8" width="440" height="410" rx="24" fill="#eef8ff"/><line x1="48" y1="382" x2="412" y2="382" stroke="#91b7cf" stroke-width="6"/><text x="55" y="407" font-size="18" fill="#35536c">ゆか</text>
      <path d="M235 250 L225 368 L194 376M253 250 L264 368 L294 376" fill="none" stroke="#284b70" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="235" cy="250" r="14" fill="#ff9f43" stroke="white" stroke-width="4"/>
      <path d="M235 250 L{shoulder_x:.1f} {shoulder_y:.1f}" stroke="white" stroke-width="68" stroke-linecap="round"/><path d="M235 250 L{shoulder_x:.1f} {shoulder_y:.1f}" stroke="#35536c" stroke-width="4" stroke-linecap="round"/>
      <circle cx="{head_x:.1f}" cy="{head_y:.1f}" r="31" fill="#ffd9b8" stroke="#35536c" stroke-width="4"/><path d="M{head_x-25:.1f} {head_y-8:.1f} Q{head_x:.1f} {head_y-38:.1f} {head_x+26:.1f} {head_y-7:.1f}" fill="#39495a" stroke="#39495a" stroke-width="8" stroke-linecap="round"/>
      <path d="M{arm_x:.1f} {shoulder_y+5:.1f} L{arm_x-5:.1f} {hand_y:.1f}M{arm_x+22:.1f} {shoulder_y+7:.1f} L{arm_x+26:.1f} {hand_y:.1f}" fill="none" stroke="#ffd9b8" stroke-width="20" stroke-linecap="round"/>
      <path d="M165 225 A88 88 0 0 0 120 143" fill="none" stroke="#33a7d8" stroke-width="7" stroke-linecap="round" stroke-dasharray="10 9"/><path d="M108 151 L117 125 L136 145" fill="#33a7d8"/>
      <text x="53" y="92" font-size="21" font-weight="700" fill="#1769c2">{words}</text><text x="253" y="244" font-size="17" font-weight="700" fill="#c56616">こしから</text><text x="300" y="344" font-size="17" font-weight="700" fill="#35536c">ひざは まっすぐ</text>
    </svg>"""

pages = ["1. そくわんしょうって なに？", "2. まえに かがんでみよう", "3. どこを みるの？", "4. あんしんして うける", "5. わかったかな？"]
page = st.sidebar.radio("がくしゅう メニュー", pages)

if page == pages[0]:
    hero("そくわんしょうの けんしんを しろう", "なにを するのか、いっしょに みてみよう")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="card"><h3>🦴 せぼねの かたちを みるよ</h3><p>せぼねが よこに まがったり、ねじれたり していないか みます。<br>はやく みつけるための けんしんです。</p></div><div class="notice"><b>この けんしんだけで、びょうきを きめるわけでは ないよ。</b></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(back_figure(False, True), unsafe_allow_html=True)
    st.markdown("### おいしゃさんが みる ところ")
    cols = st.columns(4)
    for col, icon, label in zip(cols, ["↔️", "🪽", "〰️", "🔎"], ["かたの たかさ", "せなかの ほね", "こしの かたち", "せなかの たかさ"]):
        col.markdown(f'<div class="card" style="text-align:center"><h2>{icon}</h2><b>{label}</b></div>', unsafe_allow_html=True)

elif page == pages[1]:
    hero("まえに かがんでみよう", "あしは そのまま。こしから ゆっくり まえへ。")
    angle = st.slider("からだを まえに たおす", 0, 90, 0, 5, format="%d°")
    c1, c2 = st.columns([1.25, 1])
    with c1:
        st.markdown(forward_bend_figure(angle), unsafe_allow_html=True)
    with c2:
        if angle < 20: message = "① あしを そろえて、まっすぐ たつよ。"
        elif angle < 55: message = "② ひざを のばして、ゆっくり まえへ。"
        elif angle < 80: message = "③ てを したへ。いたいときは とまってね。"
        else: message = "④ できた！ ちからを ぬいて、そのまま まつよ。"
        st.markdown(f'<div class="card"><h3>{message}</h3></div>', unsafe_allow_html=True)
        st.progress(angle / 90)
        st.markdown('<div class="notice"><b>だいじなこと</b><br>いたいときや こわいときは、<b>「とめて」</b>と いっていいよ。</div>', unsafe_allow_html=True)

elif page == pages[2]:
    hero("どこを みているの？", "みぎと ひだりの ちがいを みるよ")
    different = st.toggle("みぎと ひだりが ちがう れいを みる")
    points = st.checkbox("みる ところに あかい まるを つける", value=True)
    c1, c2 = st.columns(2)
    with c1: st.markdown(back_figure(different, points), unsafe_allow_html=True)
    with c2:
        observations = {"かた":"かたの たかさが、おなじか みます。", "せなかの ほね":"せなかの ほねの たかさや ばしょを みます。", "こし":"こしの かたちが、おなじか みます。", "かがんだときの せなか":"せなかの かたほうが、たかく ないか みます。"}
        selected = st.radio("どこを みる？", list(observations))
        st.markdown(f'<div class="card"><h3>{selected}</h3><p>{observations[selected]}</p></div>', unsafe_allow_html=True)
        st.info("ちがいが みえても、この がめんだけで びょうきを きめることは できません。")

elif page == pages[3]:
    hero("あんしんして うけるために", "こまったときは、おとなに いっていいよ")
    items = [("🟦","ついたて・カーテン","ほかの こから、からだが みえないように するよ。"),("👕","ふくの せつめい","どんな ふくで うけるのか、まえに おしえるよ。"),("🧑‍⚕️","せんせいが いっしょ","ほけんしつの せんせいなどが、ちかくに いるよ。"),("💬","きもちを つたえる","いたい、こわい、いやなときは いっていいよ。")]
    for icon, title, body in items:
        st.markdown(f'<div class="card"><h3>{icon} {title}</h3><p>{body}</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="good"><b>あなたの からだは、あなたのものです。</b><br>わからないことは、きいてね。</div>', unsafe_allow_html=True)

else:
    hero("わかったかな？", "3もんの クイズに こたえよう")
    q1 = st.radio("1. まえに かがんで、なにを みるの？", ["えらんでね", "せなかの みぎと ひだりの ちがい", "しんちょう", "めの みえかた"])
    q2 = st.radio("2. どうやって かがむの？", ["えらんでね", "ひざを のばして ゆっくり", "いきおいよく", "いきを とめて"])
    q3 = st.radio("3. いたいときは どうする？", ["えらんでね", "おとなに つたえる", "がまんする", "はしって かえる"])
    if st.button("こたえを みる", type="primary", use_container_width=True):
        score = sum([q1 == "せなかの みぎと ひだりの ちがい", q2 == "ひざを のばして ゆっくり", q3 == "おとなに つたえる"])
        if score == 3:
            st.success("ぜんぶ せいかい！ じょうずに できました！"); st.balloons()
        else: st.warning(f"3もんの うち {score}もん せいかいです。もういちど みてみよう。")

st.divider()
st.caption("※これは けんしんの まえに べんきょうする アプリです。びょうきを きめる アプリでは ありません。")
