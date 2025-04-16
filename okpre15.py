# -*- coding: utf-8 -*-
import streamlit as st
# <<< 変更点(v1.5): CSS調整、ウィジェットカラー変更試行 >>>
# <<< 全文: CSS定義 >>>
st.markdown("""
            <style>
    /* ページ全体のコンテナ調整 */
    .block-container {
        padding-top: 1rem;
        /* max-width: 90% !important; */ /* デフォルトに戻す */
    }
    /* 中央揃えのタイトル */
    .title-center {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #246798; /* Okosyカラー */
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    /* ボタンを中央に置くラッパー (汎用) */
    .button-wrapper { /* このクラス名も残しておく (汎用的に使われている可能性) */
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
        margin-bottom: 60px;
    }
    /* 中央揃えのボタンラッパー (特定のボタン用、button-wrapperと同じ内容) */
    .center-button-wrapper {
        display: flex;
        justify-content: center;
        margin-top: 30px; /* 上の余白 */
        margin-bottom: 60px; /* 下の余白 */
    }

    /* --- Streamlitの標準ボタン (div.stButton > button) の基本スタイル --- */
    div.stButton > button {
        background-color: transparent; /* 背景は透明＝白抜き */
        color: #246798; /* テキストカラーは青 */
        border: 1.5pt solid #246798; /* 枠線も青で1.5pt */
        padding: 0.75em 2.5em; /* 内側の余白 */
        font-size: 20px; /* 文字サイズ */
        font-weight: bold; /* 太字 */
        border-radius: 10px; /* 角丸 */
        transition: transform 0.2s ease, background-color 0.4s ease, color 0.4s ease; /* アニメーション */
        width: auto; /* ★★★ 維持: ボタン幅は内容に合わせる ★★★ */
        display: inline-block; /* ★★★ 維持: インラインブロック要素として扱う ★★★ */
        cursor: pointer; /* ★★★ 追加推奨: クリック可能であることを示すカーソル ★★★ */
    }
    /* 標準ボタンのホバー時スタイル */
    div.stButton > button:hover {
        background-color: #EAEAEA;   /* 背景は薄いグレー */
        color: #666666;           /* テキストはグレーに */
        border: none;              /* ★★★ 修正: 枠線を消す (後者の定義に合わせる) ★★★ */
        transform: scale(1.05);    /* 少し拡大 */
    }

    /* --- 特定のボタンやラッパー用のクラス --- */

    /* プランナー選択ボタンのスタイル */
    .planner-button > button {
        width: 100%; /* カラム幅いっぱいに広げる */
        margin-bottom: 10px; /* ボタン間の余白 */
        /* 基本スタイル(色、枠線など)は div.stButton > button が適用される */
    }

    /* 質問ステップ中の選択肢ボタンのスタイル */
    .choice-button > button {
        width: 100%; /* カラム幅いっぱいに広げる */
        margin-bottom: 10px; /* ボタン間の余白 */
        font-size: 16px; /* 少し小さめの文字サイズ */
        padding: 0.8em 1.5em; /* 少し小さめのパディング */
        /* 基本スタイル(色、枠線など)は div.stButton > button が適用される */
        /* ホバー時のスタイルも div.stButton > button:hover が適用される */
    }

    /* 「次へ」ボタンのラッパー */
    .next-step-button-wrapper {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    /* 「次へ」ボタン自体のスタイル (標準ボタンとほぼ同じだが、個別調整用) */
    .next-step-button > button {
        /* ここで標準ボタン(div.stButton > button)のスタイルを上書きしたい場合に追加 */
        /* 例: font-size: 18px; */
        /* 基本スタイルが適用されるので、通常は空で良い */
    }
    /* 「次へ」ボタンのホバー時スタイル (標準ホバーとほぼ同じだが、個別調整用) */
    .next-step-button > button:hover {
         /* 標準ホバー(div.stButton > button:hover)のスタイルを上書きしたい場合に追加 */
         /* 例: background-color: #DDDDDD; */
         /* 基本ホバースタイルが適用されるので、通常は空で良い */
    }

    /* 「生成」ボタンのラッパー */
    .generate-button-wrapper {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }
    /* 「生成」ボタン自体のスタイル (標準ボタンを上書き) */
    .generate-button > button {
        background-color: #246798; /* 背景色: 青 */
        color: white; /* 文字色: 白 */
        border: none; /* ★★★ 枠線なし ★★★ */
        padding: 1em 3em; /* パディング大きめ */
        font-size: 22px; /* 文字サイズ大きめ */
        font-weight: bold;
        border-radius: 12px; /* 角丸少し大きめ */
        transition: transform 0.2s ease, background-color 0.4s ease;
        /* width, display は標準の div.stButton > button から継承(上書きしない限り) */
    }
    /* 「生成」ボタンのホバー時スタイル */
    .generate-button > button:hover {
        background-color: #1E537A; /* 背景色: 少し濃い青 */
        color: white; /* 文字色は白のまま */
        transform: scale(1.05); /* 少し拡大 */
        border: none; /* ★★★ 枠線なし (念のため) ★★★ */
    }

    /* --- Streamlitウィジェットの調整 & カラー変更の試み --- */
    /* (この部分は変更なし) */
    .stRadio > div { display: flex; flex-direction: column; }
    .stRadio > label { font-weight: bold; margin-bottom: 10px; }
    .stRadio > div > div { display: flex; align-items: center; margin-bottom: 5px; }
    /* ラジオボタン選択円の色(試み) */
    div[data-testid="stRadio"] input[type="radio"]:checked + div::before {
        background-color: #246798 !important; border-color: #246798 !important; box-shadow: inset 0.5em 0.5em #246798;
    }
    /* スライダーバーの色(試み) */
    div[data-testid="stSlider"] div[data-baseweb="slider"] > div:nth-child(3) { background-color: #246798 !important; }
    /* スライダーハンドルの色(試み) */
    div[data-testid="stSlider"] div[data-baseweb="slider"] > div:nth-child(4) { background-color: #246798 !important; border-color: #246798 !important; }
    .stSlider > label { font-weight: bold; margin-bottom: 5px; }
    /* マルチセレクトタグの色(試み) */
    div[data-testid="stMultiSelect"] div[data-baseweb="tag"] { background-color: #ADCDE3 !important; color: #1E537A !important; }
    .stMultiSelect > label { font-weight: bold; margin-bottom: 5px; }
    .stTextArea > label { font-weight: bold; margin-bottom: 5px; }
    .stTextInput > label { font-weight: bold; margin-bottom: 5px; }
    .stFileUploader > label { font-weight: bold; margin-bottom: 10px; }
    .stNumberInput > label { font-weight: bold; margin-bottom: 5px; }

    </style>
""", unsafe_allow_html=True)

# --- 1. 必要なライブラリのインポート ---
# <<< 全文: インポート文 >>>
import openai
from openai import OpenAI
import requests
import json
import os
import datetime
from dotenv import load_dotenv
from PIL import Image
import io
import pandas as pd
import random
import time
import base64
import traceback
from typing import Optional, List, Dict, Any
from collections import Counter # <<< 追加(v1.5)
import statistics # <<< 追加(v1.5)


# Firebase 関連ライブラリ
import firebase_admin
from firebase_admin import credentials, auth, firestore
# Streamlit Firebase Auth コンポーネント
try: import streamlit_firebase_auth as sfa
except ImportError: st.error("認証ライブラリ未検出"); sfa = None
except Exception as e: st.error(f"認証ライブラリImportエラー: {e}"); sfa = None

# Google Cloud Vision
try:
    from google.cloud import vision
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
except ImportError: st.error("Visionライブラリ未検出"); vision = None; service_account = None; Request = None

# --- ヘッダー画像表示 ---
# <<< 全文: ヘッダー画像表示関数と呼び出し >>>
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as f: data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError: st.warning(f"ヘッダー画像未検出: {image_path}"); return None
    except Exception as e: st.warning(f"ヘッダー画像読込エラー: {e}"); return None
header_base64 = get_base64_image("assets/header_okosy.png")
if header_base64: st.markdown( f""" <div style="text-align: center; margin-top: 30px; margin-bottom: 100px;"> <img src="data:image/png;base64,{header_base64}" width="700" style="border-radius: 8px;"> </div> """, unsafe_allow_html=True )

# --- 1. 環境変数の読み込みと初期設定 ---
# <<< 全文: 環境変数読み込みと設定 >>>
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
SERVICE_ACCOUNT_KEY_PATH = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY_PATH", "path/to/your/serviceAccountKey.json")
FIREBASE_CONFIG_PATH = os.getenv("FIREBASE_CONFIG_PATH", "path/to/your/firebase_config.json")

# --- 認証設定 (Vision API用) ---
if SERVICE_ACCOUNT_KEY_PATH and os.path.exists(SERVICE_ACCOUNT_KEY_PATH):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY_PATH
    print(f"GCreds set: {SERVICE_ACCOUNT_KEY_PATH}")
else: print(f"Warning: Service account key path not found: {SERVICE_ACCOUNT_KEY_PATH}")

# APIキーの存在チェック
if not OPENAI_API_KEY: st.error("OpenAI APIキー未検出"); st.stop()
if not GOOGLE_PLACES_API_KEY: st.error("Google Places APIキー未検出"); st.stop()

# --- OpenAI クライアント初期化 ---
try: client = OpenAI(api_key=OPENAI_API_KEY)
except Exception as e: st.error(f"OpenAIクライアント初期化失敗: {e}"); st.stop()

# --- 2. Firebase Admin SDK の初期化 ---
# <<< 全文: Firebase Admin SDK初期化 >>>
if not firebase_admin._apps:
    if not os.path.exists(SERVICE_ACCOUNT_KEY_PATH): st.error(f"Firebase SAキー未検出: {SERVICE_ACCOUNT_KEY_PATH}"); st.stop()
    try:
        cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
        firebase_admin.initialize_app(cred)
        print("Firebase Admin SDK initialized.")
    except Exception as e: st.error(f"Firebase Admin SDK 初期化失敗: {e}"); st.error(traceback.format_exc()); st.stop()

# --- 2.1 Firebase Web アプリ設定の読み込み ---
# <<< 全文: Firebase Web設定読み込み >>>
firebase_config = None
if not os.path.exists(FIREBASE_CONFIG_PATH): st.error(f"Firebase Web 設定未検出: {FIREBASE_CONFIG_PATH}"); st.stop()
else:
    try:
        with open(FIREBASE_CONFIG_PATH) as f: firebase_config = json.load(f)
    except Exception as e: st.error(f"Firebase Web 設定読込失敗: {e}"); st.stop()

# --- 2.2 streamlit-firebase-auth コンポーネントの初期化 ---
# <<< 全文: streamlit-firebase-auth初期化 >>>
auth_obj = None
if sfa is None: st.error("認証機能初期化失敗 (sfa is None)"); st.stop()
if firebase_config is None: st.error("Firebase Web設定未読込"); st.stop()
try: auth_obj = sfa.FirebaseAuth(firebase_config)
except Exception as e: st.error(f"FirebaseAuth オブジェクト作成失敗: {e}"); st.error(traceback.format_exc()); st.stop()

# --- 2.3 Firestore クライアントの初期化 ---
# <<< 全文: Firestoreクライアント初期化 >>>
try: db = firestore.client(); print("Firestore client initialized.")
except Exception as e: st.error(f"Firestore クライアント初期化失敗: {e}"); st.error(traceback.format_exc()); st.stop()

# --- Firestore データ操作関数 ---
# <<< 全文: Firestore関連関数定義 >>>
def save_itinerary_to_firestore(user_id: str, name: str, preferences: dict, generated_content: str, places_data: Optional[str]):
    """しおりデータをFirestoreに保存する"""
    if not db: st.error("Firestoreクライアント未初期化"); return None
    try:
        doc_ref = db.collection("users").document(user_id).collection("itineraries").document()
        doc_ref.set({
            "name": name, "preferences": json.dumps(preferences, ensure_ascii=False), # <<< 変更点(v1.5): 保存する好み情報 >>>
            "generated_content": generated_content, "places_data": places_data if places_data else None,
            "creation_date": firestore.SERVER_TIMESTAMP # type: ignore
        })
        print(f"Itinerary saved: {user_id}, {doc_ref.id}"); return doc_ref.id
    except Exception as e: st.error(f"Firestore保存エラー: {e}"); print(traceback.format_exc()); return None

def load_itineraries_from_firestore(user_id: str):
    """指定したユーザーのしおり一覧をFirestoreから読み込む (最新20件)"""
    if not db: return []
    itineraries = []
    try:
        itineraries_ref = db.collection("users").document(user_id).collection("itineraries").order_by(
            "creation_date", direction=firestore.Query.DESCENDING # type: ignore
        ).limit(20).stream() # <<< 変更点(v1.5): コスト/パフォーマンスのため最新20件に制限 >>>
        for doc in itineraries_ref:
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                try: data['preferences_dict'] = json.loads(data.get('preferences', '{}')) # <<< 変更点(v1.5): 好み情報を読み込む >>>
                except (json.JSONDecodeError, TypeError): data['preferences_dict'] = {}
                itineraries.append(data)
        return itineraries
    except Exception as e: st.error(f"Firestore読込エラー: {e}"); print(traceback.format_exc()); return []

def delete_itinerary_from_firestore(user_id: str, itinerary_id: str):
    """指定したしおりと関連する思い出をFirestoreから削除する"""
    if not db: return False
    try:
        memories_ref = db.collection("users").document(user_id).collection("itineraries").document(itinerary_id).collection("memories").stream()
        batch_mem = db.batch(); mem_deleted_count = 0
        for mem_doc in memories_ref: batch_mem.delete(mem_doc.reference); mem_deleted_count += 1
        if mem_deleted_count > 0: batch_mem.commit(); print(f"Deleted {mem_deleted_count} memories for {itinerary_id}")
        db.collection("users").document(user_id).collection("itineraries").document(itinerary_id).delete()
        print(f"Itinerary deleted: {user_id}, {itinerary_id}"); return True
    except Exception as e: st.error(f"Firestore削除エラー: {e}"); print(traceback.format_exc()); return False

def save_memory_to_firestore(user_id: str, itinerary_id: str, caption: str, photo_base64: Optional[str]):
    """思い出データをFirestoreに保存する"""
    if not db: return None
    try:
        doc_ref = db.collection("users").document(user_id).collection("itineraries").document(itinerary_id).collection("memories").document()
        doc_ref.set({ "caption": caption, "photo_base64": photo_base64, "creation_date": firestore.SERVER_TIMESTAMP }) # type: ignore
        print(f"Memory saved: {itinerary_id}, {doc_ref.id}"); return doc_ref.id
    except Exception as e: st.error(f"Firestore思い出保存エラー: {e}"); print(traceback.format_exc()); return None

def load_memories_from_firestore(user_id: str, itinerary_id: str):
    """指定したしおりの思い出一覧をFirestoreから読み込む"""
    if not db: return []
    memories = []
    try:
        memories_ref = db.collection("users").document(user_id).collection("itineraries").document(itinerary_id).collection("memories").order_by(
            "creation_date", direction=firestore.Query.DESCENDING ).stream() # type: ignore
        for doc in memories_ref:
            data = doc.to_dict()
            if data:
                data['id'] = doc.id; photo_b64 = data.get('photo_base64')
                if photo_b64:
                    try: img_bytes = base64.b64decode(photo_b64); data['photo_image'] = Image.open(io.BytesIO(img_bytes))
                    except Exception as img_e: print(f"Error decode image {doc.id}: {img_e}"); data['photo_image'] = None
                else: data['photo_image'] = None
                memories.append(data)
        return memories
    except Exception as e: st.error(f"Firestore思い出読込エラー: {e}"); print(traceback.format_exc()); return []

def delete_memory_from_firestore(user_id: str, itinerary_id: str, memory_id: str):
    """指定した思い出をFirestoreから削除する"""
    if not db: return False
    try:
        db.collection("users").document(user_id).collection("itineraries").document(itinerary_id).collection("memories").document(memory_id).delete()
        print(f"Memory deleted: {itinerary_id}, {memory_id}"); return True
    except Exception as e: st.error(f"Firestore思い出削除エラー: {e}"); print(traceback.format_exc()); return False

# <<< 変更点(v1.5): 過去の好み情報を読み込み、デフォルト値として設定する関数 >>>
def load_and_set_default_preferences(user_id: str, question_definitions: List[Dict]):
    """Firestoreから過去しおり(最大20件)を読み込み、今回の質問デフォルト値を設定"""
    print(f"Loading past preferences for user: {user_id}")
    past_itineraries = load_itineraries_from_firestore(user_id)
    if not past_itineraries: print("No past itineraries found."); return

    past_prefs = {q_def["key"]: [] for q_def in question_definitions}
    for itin in past_itineraries:
        prefs_dict = itin.get('preferences_dict', {})
        if isinstance(prefs_dict, dict):
             for q_def in question_definitions:
                 q_key = q_def["key"]
                 pref_key_in_dict = next((k for k, v in PREF_KEY_MAP.items() if v == q_key), None) # PREF_KEY_MAPを使用
                 if pref_key_in_dict and pref_key_in_dict in prefs_dict:
                     value = prefs_dict[pref_key_in_dict]
                     if value is not None: past_prefs[q_key].append(value)

    # print(f"Collected past preferences: {past_prefs}") # デバッグ出力抑制

    for q_def in question_definitions:
        q_key = q_def["key"]; q_type = q_def["type"]; values = past_prefs.get(q_key, [])
        if not values: continue
        default_value = None
        try:
            if q_type in ["button_choice", "radio"]: # <<< 変更点(v1.6): button_choiceも対象に >>>
                if values: default_value = Counter(values).most_common(1)[0][0]
            elif q_type == "number_input" or q_type == "slider":
                numeric_values = [v for v in values if isinstance(v, (int, float))]
                if numeric_values:
                    default_value = round(statistics.mean(numeric_values))
                    if "min" in q_def and default_value < q_def["min"]: default_value = q_def["min"]
                    if "max" in q_def and default_value > q_def["max"]: default_value = q_def["max"]
            elif q_type == "multiselect":
                all_selected_items = [item for sublist in values for item in sublist if isinstance(sublist, list)]
                if all_selected_items:
                    valid_options = set(q_def.get("options", []))
                    valid_selected_items = [item for item in all_selected_items if item in valid_options]
                    if valid_selected_items: default_value = [item for item, count in Counter(valid_selected_items).most_common(3)]
            elif q_type == "text_input":
                 if values: default_value = values[-1] # 最新の値
        except Exception as e: print(f"Error calc default for {q_key}: {e}"); default_value = None
        if default_value is not None:
            st.session_state[q_key] = default_value
            print(f"Set default for {q_key}: {default_value}")

# --- 3. 認証処理とログイン状態の管理 ---
# <<< 全文: 認証処理 >>>
if 'user_info' not in st.session_state: st.session_state['user_info'] = None
if 'id_token' not in st.session_state: st.session_state['id_token'] = None

if st.session_state['user_info'] is None:
    st.subheader("Googleアカウントでログイン")
    st.write("Okosy を利用するには、Googleアカウントでのログインが必要です。")
    st.info("下のフォームの「Sign in with Google」ボタンをクリックしてください。")
    if auth_obj is None: st.error("認証オブジェクト未初期化"); st.stop()
    try:
        login_result = auth_obj.login_form()
        if login_result and isinstance(login_result, dict) and login_result.get('success') is True:
            user_data = login_result.get('user'); token_manager = user_data.get('stsTokenManager') if user_data else None
            id_token = token_manager.get('accessToken') if token_manager else None
            if id_token:
                st.session_state['id_token'] = id_token
                try:
                    decoded_token = auth.verify_id_token(st.session_state['id_token'])
                    st.session_state['user_info'] = decoded_token
                    st.success("ログインしました！"); print(f"User logged in: {decoded_token.get('uid')}")
                    time.sleep(1); st.rerun()
                except Exception as e: st.error(f"ログインエラー (トークン検証失敗): {e}"); print(f"Token verify failed: {e}"); st.session_state['id_token'] = None; st.session_state['user_info'] = None
            else: st.error("ログイン成功しましたが、トークンが見つかりません。"); print("AccessToken not found.")
        elif login_result and isinstance(login_result, dict) and login_result.get('success') is False:
            error_message = login_result.get('error', '不明なエラー')
            if 'auth/popup-closed-by-user' in str(error_message): st.warning("ポップアップが閉じられたかブロックされました。")
            elif 'auth/cancelled-popup-request' in str(error_message): st.warning("ログインリクエストがキャンセルされました。")
            else: st.error(f"ログイン失敗: {error_message}")
            print(f"Login failed: {error_message}")
    except Exception as e: st.error(f"認証フォーム処理エラー: {e}"); st.error(traceback.format_exc())
    st.stop()

# --- 3.1 ログイン後のメインコンテンツ ---
# <<< 全文: ログイン後メインコンテンツ処理 >>>
if st.session_state.get('user_info') is not None:
    user_id = st.session_state['user_info'].get('uid')
    if not user_id: st.error("ユーザーID取得不可"); st.session_state['user_info'] = None; st.session_state['id_token'] = None; st.rerun()

    # --- サイドバーの設定 (ログイン後) ---
    st.sidebar.header("メニュー")
    user_email = st.session_state['user_info'].get('email', '不明')
    st.sidebar.write(f"ログイン中: {user_email}")
    if st.sidebar.button("ログアウト"):
        st.session_state['user_info'] = None; st.session_state['id_token'] = None
        # <<< 変更点(v1.5): クリアするキーリスト (`purp`削除) >>>
        keys_to_clear = [ "itinerary_generated", "generated_shiori_content", "final_places_data", "preferences_for_prompt", "determined_destination", "determined_destination_for_prompt", "messages_for_prompt", "shiori_name_input", "selected_itinerary_id", "selected_itinerary_id_selector", "show_planner_select", "planner_selected", "planner", "current_question_step", "messages", "preferences", "dest", "comp", "days", "budg", "pref_nature", "pref_culture", "pref_art", "pref_welness", "pref_food_local", "pref_food_style", "pref_accom_type", "pref_word", "mbti", "free_request", "pref_food_style_ms", "pref_word_ms", "mbti_input", "uploaded_image_files", "q0_sea_mountain", "q1_style", "q2_atmosphere", "memory_caption", "memory_photo", "defaults_loaded" ]
        for key in keys_to_clear:
            if key in st.session_state: del st.session_state[key]
        st.success("ログアウトしました。"); print("User logged out.")
        time.sleep(1); st.rerun()
    st.sidebar.markdown("---")
    menu_choice = st.sidebar.radio("", ["新しい旅を計画する", "過去の旅のしおりを見る"], key="main_menu", label_visibility="collapsed")
    st.sidebar.image("assets/logo_okosy.png", width=100)

    # --- 4. Google Maps関連のヘルパー関数 ---
    # <<< 全文: get_coordinates関数 >>>
    def get_coordinates(address):
        """住所から緯度経度取得"""
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {"address": address, "key": GOOGLE_PLACES_API_KEY, "language": "ja", "region": "JP"}
        try:
            res = requests.get(url, params=params, timeout=10); res.raise_for_status(); results = res.json()
            if results["status"] == "OK" and results["results"]: loc = results["results"][0]["geometry"]["location"]; return f"{loc['lat']},{loc['lng']}"
            else: print(f"Geocoding fail: {results.get('status')}, {results.get('error_message', '')}"); return None
        except requests.exceptions.Timeout: print(f"Geocoding timeout: {address}"); return None
        except requests.exceptions.RequestException as e: print(f"Geocoding HTTP err: {e}"); return None
        except Exception as e: print(f"Geocoding unexpected err: {e}"); return None

    # --- Vision API ラベル抽出関数 ---
    # <<< 全文: get_vision_labels_from_uploaded_images関数 >>>
    def get_vision_labels_from_uploaded_images(image_files):
        """画像からVision APIでラベル抽出"""
        gac_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not vision or not service_account or not Request: st.warning("Visionライブラリ未検出"); return []
        if not gac_path: st.warning("Vision認証情報(env)未設定"); return []
        if not os.path.exists(gac_path): st.warning(f"Vision認証ファイル未検出: {gac_path}"); return []
        try:
            creds = service_account.Credentials.from_service_account_file(gac_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])
            if not creds.valid: creds.refresh(Request())
            token = creds.token; endpoint = "https://vision.googleapis.com/v1/images:annotate"; all_labels = []; count = 0
            for img_file in image_files:
                try:
                    if hasattr(img_file, 'seek'): img_file.seek(0)
                    content = base64.b64encode(img_file.read()).decode("utf-8")
                    payload = {"requests": [{"image": {"content": content}, "features": [{"type": "LABEL_DETECTION", "maxResults": 5}]}]}
                    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
                    res = requests.post(endpoint, headers=headers, json=payload, timeout=20)
                    if res.status_code == 200:
                        data = res.json()
                        if data.get("responses") and data["responses"][0]: labels = [ann["description"] for ann in data["responses"][0].get("labelAnnotations", [])]; all_labels.extend(labels); count += 1
                        else: print(f"Vision API: Invalid response {data}")
                    else: print(f"Vision API REST err: {res.status_code}, {res.text}")
                except requests.exceptions.Timeout: st.warning(f"Vision APIタイムアウト (1画像)"); print("Vision timeout"); continue
                except Exception as img_e: st.warning(f"個別画像処理エラー: {img_e}"); print(f"Vision img err: {img_e}"); continue
            unique_labels = list(set(all_labels)); print(f"Vision processed {count}/{len(image_files)}. Labels: {unique_labels[:10]}"); return unique_labels[:10]
        except Exception as e: st.error(f"Vision API全体エラー: {e}"); print(f"Vision overall err: {e}"); print(traceback.format_exc()); return []

    # --- Google Places API 検索関数 ---
    # <<< 全文: search_google_places関数 >>>
    def search_google_places(query: str, location_bias: Optional[str] = None, place_type: str = "tourist_attraction", min_rating: Optional[float] = 4.0, price_levels: Optional[str] = None) -> str:
        """Google Places Text Search"""
        print(f"--- Calling Places API: Q={query}, Loc={location_bias}, Type={place_type}, Rate={min_rating}, Price={price_levels} ---")
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {"query": query, "key": GOOGLE_PLACES_API_KEY, "language": "ja", "region": "JP", "type": place_type}
        if location_bias: params["location"] = location_bias; params["radius"] = 20000
        try:
            res = requests.get(url, params=params, timeout=15); res.raise_for_status(); results = res.json(); status = results.get("status")
            if status == "OK":
                filtered = []; count = 0
                for place in results.get("results", []):
                    rating = place.get("rating", 0); price = place.get("price_level")
                    if min_rating is not None and rating < min_rating: continue
                    if price_levels:
                        try:
                            allowed = [int(x.strip()) for x in price_levels.split(',') if x.strip().isdigit()]; P = price; R = rating
                            if P is not None and P not in allowed: continue
                        except ValueError: print(f"Invalid price_levels: {price_levels}")
                    filtered.append({ "name": place.get("name"), "address": place.get("formatted_address"), "rating": rating, "price_level": price, "types": place.get("types", []), "place_id": place.get("place_id") }); count += 1
                    if count >= 5: break
                if not filtered: print("Places: No results match criteria."); return json.dumps({"message": "条件合致場所なし"}, ensure_ascii=False)
                else: print(f"Places: Found {len(filtered)}"); return json.dumps(filtered, ensure_ascii=False)
            elif status == "ZERO_RESULTS": print("Places: ZERO_RESULTS."); return json.dumps({"message": "検索結果0件"}, ensure_ascii=False)
            else: err_msg = results.get('error_message', ''); print(f"Places API err: {status}, {err_msg}"); return json.dumps({"error": f"Places API Error: {status}, {err_msg}"}, ensure_ascii=False)
        except requests.exceptions.Timeout: print(f"Places API timeout: {query}"); return json.dumps({"error": "Places APIタイムアウト"}, ensure_ascii=False)
        except requests.exceptions.RequestException as e: print(f"Places API HTTP err: {e}"); return json.dumps({"error": f"Places API接続HTTPエラー: {e}"}, ensure_ascii=False)
        except Exception as e: print(f"Places unexpected err: {e}"); print(traceback.format_exc()); return json.dumps({"error": f"場所検索中予期せぬエラー: {e}"}, ensure_ascii=False)

    # --- 5. OpenAI Function Calling (Tool Calling) 準備 ---
    # <<< 全文: OpenAI toolsとavailable_functions定義 >>>
    tools = [ { "type": "function", "function": { "name": "search_google_places", "description": "Google Places APIで場所検索", "parameters": { "type": "object", "properties": { "query": {"type": "string", "description": "検索語(例:'京都抹茶')"}, "location_bias": {"type": "string", "description": "中心座標(緯度,経度 例:'35.0,135.7')"}, "place_type": { "type": "string", "description": "場所タイプ", "enum": [ "tourist_attraction", "restaurant", "lodging", "cafe", "museum", "park", "art_gallery", "store", "bar", "spa" ] }, "min_rating": {"type": "number", "description": "最低評価(例:4.0)"}, "price_levels": {"type": "string", "description": "価格帯カンマ区切り(例:'1,2')"} }, "required": ["query", "place_type"] } } } ]
    available_functions = { "search_google_places": search_google_places }

    # --- OpenAI API 会話実行関数 (Vision API連携版) ---
    # <<< 全文: run_conversation_with_function_calling関数 >>>
    def run_conversation_with_function_calling(messages: List[Dict[str, Any]], uploaded_image_files: Optional[List[Any]] = None) -> tuple[Optional[str], Optional[str]]:
        """OpenAI Tool Calling実行 (画像ラベル付与)"""
        try:
            if uploaded_image_files:
                print(f"--- Processing {len(uploaded_image_files)} images ---")
                try:
                    labels = get_vision_labels_from_uploaded_images(uploaded_image_files)
                    if labels:
                        label_text = "【画像特徴(参考)】\n" + ", ".join(labels); print(f"Labels: {label_text}")
                        last_msg = messages[-1]
                        if isinstance(last_msg.get('content'), str):
                            if "【画像特徴(参考)】" not in last_msg['content']: last_msg['content'] += "\n\n" + label_text
                        elif isinstance(last_msg.get('content'), list):
                            found = False
                            for item in last_msg['content']:
                                if item.get("type") == "text":
                                    if "【画像特徴(参考)】" not in item.get("text",""): item["text"] = item.get("text","") + "\n\n" + label_text
                                    found = True; break
                            if not found: last_msg['content'].append({"type": "text", "text": label_text})
                        else: print(f"Warn: Unexpected content type: {type(last_msg.get('content'))}")
                except Exception as vision_e: st.warning(f"Vision処理エラー: {vision_e}"); print(f"Vision err: {vision_e}")

            print("--- Calling OpenAI API (1st) ---")
            response = client.chat.completions.create( model="gpt-4o", messages=messages, tools=tools, tool_choice="auto" )
            resp_msg = response.choices[0].message
            finish = response.choices[0].finish_reason
            if finish == "length": st.warning("⚠️ AI応答長すぎ")
            elif finish not in ["stop", "tool_calls"]: print(f"Warn: Finish reason: {finish}")

            tool_calls = resp_msg.tool_calls; results_list = []
            if tool_calls:
                messages.append(resp_msg.model_dump())
                for call in tool_calls:
                    func_name = call.function.name; func_to_call = available_functions.get(func_name)
                    if func_to_call:
                        try:
                            args = json.loads(call.function.arguments); print(f"Calling func: {func_name} Args: {args}")
                            if func_name == 'search_google_places' and 'location_bias' not in args:
                                try: # stがimportできない環境を考慮
                                    import streamlit as st_local
                                    if st_local.session_state.get('determined_destination_for_prompt'):
                                        coords = get_coordinates(st_local.session_state.determined_destination_for_prompt)
                                        if coords: args['location_bias'] = coords; print(f"Added bias: {coords}")
                                        else: print(f"No coords for {st_local.session_state.determined_destination_for_prompt}")
                                except (ImportError, AttributeError): print("Skip bias (no st)")
                            response_str = func_to_call(**args); results_list.append(response_str)
                            messages.append({ "tool_call_id": call.id, "role": "tool", "name": func_name, "content": response_str })
                        except json.JSONDecodeError as json_e: print(f"Err decode JSON args {func_name}: {call.function.arguments}. Err: {json_e}"); err_content = json.dumps({"error": f"Arg decode err: {json_e}"}, ensure_ascii=False); results_list.append(err_content); messages.append({ "tool_call_id": call.id, "role": "tool", "name": func_name, "content": err_content })
                        except Exception as e: print(f"Err exec func {func_name}: {e}"); print(traceback.format_exc()); err_content = json.dumps({"error": f"Func exec err: {str(e)}"}, ensure_ascii=False); results_list.append(err_content); messages.append({ "tool_call_id": call.id, "role": "tool", "name": func_name, "content": err_content })
                    else: print(f"Err: Func '{func_name}' not found."); err_content = json.dumps({"error": f"Func '{func_name}' not found."}, ensure_ascii=False); results_list.append(err_content); messages.append({ "tool_call_id": call.id, "role": "tool", "name": func_name, "content": err_content })

                print("--- Sending tool results back to OpenAI (2nd) ---")
                second_res = client.chat.completions.create(model="gpt-4o", messages=messages)
                final_content = second_res.choices[0].message.content
                finish2 = second_res.choices[0].finish_reason
                if finish2 == "length": st.warning("⚠️ AI応答長すぎ(2nd)")
                elif finish2 != "stop": print(f"Warn: Finish reason(2nd): {finish2}")
                valid_json_res = [];
                for res_str in results_list:
                    try: json.loads(res_str); valid_json_res.append(res_str)
                    except json.JSONDecodeError: print(f"Warn: Skip invalid JSON: {res_str}")
                final_places_str = json.dumps(valid_json_res, ensure_ascii=False) if valid_json_res else None
                return final_content, final_places_str
            else: print("--- No tool call ---"); final_content = resp_msg.content; return final_content, None
        except openai.APIError as e: st.error(f"OpenAI APIエラー: {e.status_code}, {e.message}"); print(f"OpenAI API Err: {e.status_code}, {e.type}, {e.message}");
        if e.response and hasattr(e.response, 'text'):
            print(f"API Body: {e.response.text}");
            return f"AI通信APIエラー: {e.message}", None
        return "処理中予期せぬエラー", None

    # --- 6. Streamlitの画面構成 ---
    # <<< 全文: 画面構成関連の定義 >>>
    if "all_prefectures" not in st.session_state: st.session_state.all_prefectures = ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]

    # <<< 変更点(v1.6): 質問定義更新 (`purp`削除、一部radioをbutton_choiceに変更) >>>
    question_definitions = [
        {"step": 1, "key": "comp", "type": "button_choice", "label": "👥 誰と行きますか？", "options": ["一人旅", "夫婦・カップル", "友人", "家族"]},
        {"step": 2, "key": "days", "type": "number_input", "label": "📅 何日間ですか？", "min": 1, "max": 30, "default": 2},
        {"step": 3, "key": "budg", "type": "button_choice", "label": "💰 予算感は？", "options": ["気にしない", "安め", "普通", "高め"], "default": "普通"},
        {"step": 4, "key": "q0_sea_mountain", "type": "button_choice", "label": "🌊 Q1: 海と山、どっち派？", "options": ["海", "山", "どちらでも"]}, # type変更
        {"step": 5, "key": "q1_style", "type": "button_choice", "label": "🏃 Q2: 旅のスタイルは？", "options": ["アクティブに観光", "ゆったり過ごす"]}, # type変更
        {"step": 6, "key": "q2_atmosphere", "type": "button_choice", "label": "🌸 Q3: どんな雰囲気を感じたい？", "options": ["和の雰囲気", "モダン・都会的", "特にこだわらない"]}, # type変更
        {"step": 7, "key": "pref_nature", "type": "slider", "label": "🌲 自然が好き", "min": 1, "max": 5, "default": 3},
        {"step": 8, "key": "pref_culture", "type": "slider", "label": "🏯 歴史・文化が好き", "min": 1, "max": 5, "default": 3},
        {"step": 9, "key": "pref_art", "type": "slider", "label": "🎨 アートが好き", "min": 1, "max": 5, "default": 3},
        {"step": 10, "key": "pref_welness", "type": "slider", "label": "♨️ 癒やされたい (ウェルネス)", "min": 1, "max": 5, "default": 3},
        {"step": 11, "key": "pref_food_local", "type": "button_choice", "label": "🍽️ 食事場所の好みは？", "options": ["地元の人気店", "隠れ家的なお店", "こだわらない"], "default": "地元の人気店"}, # type変更
        {"step": 12, "key": "pref_food_style", "type": "multiselect", "label": "🍲 好きな料理・ジャンルは？ (複数可)", "options": ["和食", "洋食", "カフェ", "スイーツ", "郷土料理", "エスニック", "ラーメン", "寿司"], "key_suffix": "_ms"},
        {"step": 13, "key": "pref_accom_type", "type": "button_choice", "label": "🏨 泊まりたい宿のタイプは？", "options": ["ホテル", "旅館", "民宿・ゲストハウス", "こだわらない"], "default": "ホテル"}, # type変更
        {"step": 14, "key": "pref_word", "type": "multiselect", "label": "✨ 気になるキーワードは？ (複数可)", "options": ["隠れた発見", "カラフル", "静かで落ち着いた", "冒険", "定番", "温泉", "寺社仏閣", "食べ歩き","ショッピング","日本酒","ワイン", "おこもり","子供と楽しむ", "ローカル体験", "アウトドア","写真映え", "パワースポット"], "key_suffix": "_ms"},
        {"step": 15, "key": "mbti", "type": "text_input", "label": "🧠 あなたのMBTIは？ (任意)", "key_suffix": "_input", "help": "例: ENFP 性格タイプに合わせて提案が変わるかも？"},
        {"step": 16, "key": "uploaded_image_files", "type": "file_uploader", "label": "🖼️ 行きたい場所のイメージに近い画像をアップロード (任意・3枚まで)", "file_types": ["jpg", "jpeg", "png"]},
        {"step": 17, "key": "free_request", "type": "text_area", "label": "📝 その他、プランナーへの要望があればどうぞ！"}
    ]
    TOTAL_QUESTION_STEPS = len(question_definitions)

    # <<< 変更点(v1.5): Firestore保存キーとSession Stateキーのマッピング (`purp`削除) >>>
    PREF_KEY_MAP = {
        "同行者": "comp", "旅行日数": "days", "予算感": "budg", "海山": "q0_sea_mountain", "スタイル": "q1_style", "雰囲気": "q2_atmosphere",
        "自然": "pref_nature", "歴史文化": "pref_culture", "アート": "pref_art", "ウェルネス": "pref_welness", "食事場所": "pref_food_local",
        "料理ジャンル": "pref_food_style", "宿タイプ": "pref_accom_type", "気になるワード": "pref_word", "MBTI": "mbti", "自由記述": "free_request",
        "行き先": "dest" # <<< v1.5追加: 行き先もマッピングに含める (保存用) >>>
    }

    # --- セッションステート初期化 ---
    keys_to_init = [ ("show_planner_select", False), ("planner_selected", False), ("planner", None), ("messages", []), ("itinerary_generated", False), ("generated_shiori_content", None), ("final_places_data", None), ("current_question_step", 0), ("preferences", {}), ("selected_itinerary_id", None), ("preferences_for_prompt", {}), ("determined_destination", None), ("determined_destination_for_prompt", None), ("messages_for_prompt", []), ("shiori_name_input", ""), ("selected_itinerary_id_selector", None), ("main_menu", "新しい旅を計画する"), ("defaults_loaded", False) ]
    q_keys_all = [q_def["key"] for q_def in question_definitions]; # <<< 変更点(v1.5): `purp`削除後のキーリスト >>>
    for q_key in q_keys_all: keys_to_init.append((q_key, None))
    for key, default in keys_to_init:
        if key not in st.session_state: st.session_state[key] = default

    # --- メインコンテンツ ---
    # ★★★ ここからインデント修正 ★★★
    if menu_choice == "新しい旅を計画する":
        st.markdown('<div class="title-center">さあ、あなただけの旅をはじめよう。</div>', unsafe_allow_html=True)

        # --- ステップ0: プランニング開始ボタン ---
        # current_question_step が 0 で、プランナーが未選択の場合
        if st.session_state.current_question_step == 0 and not st.session_state.planner_selected:
            st.markdown('<div class="center-button-wrapper">', unsafe_allow_html=True)
            if st.button("プランニングを始める"):
                st.session_state.show_planner_select = True
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # --- プランナー選択表示 ---
        # プランナー選択画面表示フラグがTrueで、プランナーが未選択の場合
        if st.session_state.show_planner_select and not st.session_state.planner_selected:
            st.subheader("あなたにぴったりのプランナーを選んでください")
            # プランナー定義
            opts = {
                "ベテラン": {"name": "ベテラン", "prompt_persona": "経験豊富なプロとして、端的かつ的確に", "caption": "テイスト：端的シンプル。プロ感。"},
                "姉さん": {"name": "姉さん", "prompt_persona": "地元に詳しい世話好き姉さんとして、方言(例:関西弁/博多弁など行先による)を交えつつ元気に", "caption": "テイスト：地元方言＋親しみやすさ満点。"},
                "ギャル": {"name": "ギャル", "prompt_persona": "最新トレンド詳しい旅好きギャルとして、絵文字(💖✨)や若者言葉多用し、テンション高めに", "caption": "テイスト：テンション高め、語尾にハート。"},
                "王子": {"name": "王子", "prompt_persona": "あなたの旅をエスコートする王子様として、優雅で少しキザな言葉遣いで情熱的に", "caption": "テイスト：ちょっとナルシストだけど優しくリード。"}
            }
            c1, c2 = st.columns(2)
            with c1:
                for k in ["ベテラン", "姉さん"]:
                    st.markdown('<div class="planner-button">', unsafe_allow_html=True)
                    btn_lbl = f"シゴデキ{k}" if k == "ベテラン" else f"おせっかい{k}"
                    # プランナー選択ボタン
                    if st.button(btn_lbl, key=f"pl_{k}"):
                        st.session_state.planner = opts[k]
                        st.session_state.planner_selected = True
                        st.session_state.current_question_step = 1
                        st.session_state.defaults_loaded = False # デフォルト読み込み状態をリセット
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.caption(opts[k]["caption"])
            with c2:
                for k in ["ギャル", "王子"]:
                    st.markdown('<div class="planner-button">', unsafe_allow_html=True)
                    btn_lbl = f"旅好きインスタグラマー({k})" if k == "ギャル" else f"甘い言葉の{k}様"
                    # プランナー選択ボタン
                    if st.button(btn_lbl, key=f"pl_{k}"):
                        st.session_state.planner = opts[k]
                        st.session_state.planner_selected = True
                        st.session_state.current_question_step = 1
                        st.session_state.defaults_loaded = False # デフォルト読み込み状態をリセット
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.caption(opts[k]["caption"])

        # --- プランナー選択後 ---
        elif st.session_state.planner_selected:

            # --- デフォルト値読み込み処理 ---
            # 質問ステップ1以降 かつ デフォルト値がまだ読み込まれていない場合
            if st.session_state.current_question_step >= 1 and not st.session_state.defaults_loaded:
                with st.spinner("過去の好みを読み込み中..."):
                    # Firestoreなどから過去の好みを読み込む関数 (要定義)
                    load_and_set_default_preferences(user_id, question_definitions)
                    st.session_state.defaults_loaded = True
                    st.rerun() # 読み込み後に再実行して反映

            # --- しおり生成完了後: しおり表示 ---
            # しおりが生成済み かつ 内容が存在する場合
            if st.session_state.itinerary_generated and st.session_state.generated_shiori_content:
                st.header(f"旅のしおり （担当: {st.session_state.planner['name']}）")
                st.markdown(st.session_state.generated_shiori_content)
                st.markdown("---")

                # --- デバッグ用: Function Call 場所データ表示 ---
                with st.expander("▼ お店候補の表示(最大5件)", expanded=False):
                    data_str = st.session_state.final_places_data
                    if data_str:
                        try:
                            # 場所データ全体のJSONデコード試行
                            res_list = json.loads(data_str)
                            titles = ["①昼食", "②夕食", "③宿泊", "④観光"]

                            # デコード結果がリスト形式かチェック
                            if isinstance(res_list, list):
                                # リスト内の各場所データ (res_data) をループ処理
                                for i, res_data in enumerate(res_list):
                                    title = titles[i] if i < len(titles) else f"Tool{i+1}"
                                    st.subheader(title)
                                    places = None # places 変数を初期化

                                    # 各場所データの形式チェックと処理 (try...except)
                                    try:
                                        if isinstance(res_data, str):
                                            places = json.loads(res_data)
                                        elif isinstance(res_data, (list, dict)):
                                            places = res_data
                                        else:
                                            # --- 不正な形式の場合 ---
                                            st.warning(f"不正形式:{type(res_data)}")
                                            st.text(str(res_data))
                                            # ★★★ 修正点: continue を elseブロックの最後に配置 ★★★
                                            continue
                                    # --- ★★★ 修正点: except ブロックを追加 ★★★ ---
                                    except json.JSONDecodeError as json_e:
                                        st.error(f"JSONデコード失敗:{json_e}")
                                        st.text(str(res_data))
                                        # エラー時も次のループへ
                                        continue
                                    except Exception as e:
                                        st.error(f"場所データ表示エラー:{e}")
                                        st.text(str(res_data))
                                        # エラー時も次のループへ
                                        continue

                                    # places が正常に取得できた場合のみ表示処理
                                    if places is not None:
                                        if isinstance(places, list):
                                            if places:
                                                try:
                                                    df = pd.DataFrame(places)
                                                    if 'place_id' in df.columns and 'name' in df.columns:
                                                        df['場所名(リンク付き)'] = df.apply(
                                                        lambda r: f'<a href="https://www.google.com/maps/place/?q=place_id:{r["place_id"]}" target="_blank">{r["name"]}</a>'
                                                        if pd.notna(r.get('place_id')) and pd.notna(r.get('name'))
                                                        else r.get('name', ''), # place_idやnameがない場合はリンクなしのテキスト
                                                        axis=1
                                                    )
                                                     # 表示する列リストを定義 (元の 'name' と 'マップリンク' は含めない)
                                                        cols_to_display = ['場所名(リンク付き)', 'rating', 'address']
                                                    else:
                                                        st.warning("place_idまたはname欠損のためMapリンク不可")
                                                        df['場所名(リンク付き)'] = df['name'] # name列が存在すればそれをそのまま使う
                                                        cols_to_display = ['場所名(リンク付き)', 'rating', 'address'] # name列がなければ表示されない

                                                    df_disp = df[[c for c in cols_to_display if c in df.columns]].copy()
                                                    html = df_disp.to_html(escape=False, index=False, na_rep="-", justify="left")
                                                    st.markdown(html, unsafe_allow_html=True)
                                                except Exception as df_e:
                                                    st.error(f"DF表示エラー:{df_e}")
                                                    st.json(places)
                                            else:
                                                st.info("場所データ空")
                                        elif isinstance(places, dict):
                                            if "error" in places:
                                                st.error(f"エラー:{places['error']}")
                                            elif "message" in places:
                                                st.info(places['message'])
                                            else:
                                                st.json(places)
                                        else:
                                            st.warning(f"不正データ形式:{type(places)}")
                                            st.text(str(places))
                            else:
                                st.warning("場所データ形式不正(リストでない)")
                                st.text(data_str)
                        except json.JSONDecodeError:
                            st.error("場所データ全体JSONデコード失敗")
                            st.text(data_str)
                        except Exception as e:
                            st.error(f"場所データ処理エラー:{e}")
                            st.text(data_str)
                    else:
                        st.info("取得場所データなし")

                st.markdown("---")

                # --- しおり保存フォーム ---
                with st.form("save_shiori_form"):
                    default_shiori_name = f"{st.session_state.get('dest', '旅行')}のしおり"
                    shiori_name = st.text_input("しおりの名前", key="shiori_name_input", value=default_shiori_name)
                    if st.form_submit_button("このしおりを保存する"):
                        if shiori_name:
                            prefs_to_save = st.session_state.get('preferences_for_prompt', {}).copy()
                            prefs_to_save['行き先'] = st.session_state.get('dest')
                            if not prefs_to_save:
                                st.warning("保存設定情報なし")
                            else:
                                # Firestoreなどへの保存関数 (要定義)
                                saved_id = save_itinerary_to_firestore(
                                    user_id,
                                    shiori_name,
                                    prefs_to_save,
                                    st.session_state.generated_shiori_content,
                                    st.session_state.final_places_data
                                )
                                if saved_id:
                                    st.success(f"しおり「{shiori_name}」保存成功！")
                                else:
                                    st.error("しおり保存失敗")
                        else:
                            st.warning("しおりの名前を入力")

                # --- やり直しボタン ---
                if st.button("条件を変えてやり直す"):
                    keys_clr = [
                        "itinerary_generated", "generated_shiori_content", "final_places_data",
                        "preferences_for_prompt", "determined_destination", "determined_destination_for_prompt",
                        "messages_for_prompt", "shiori_name_input", "current_question_step",
                        "preferences", "dest", "comp", "days", "budg", "q0_sea_mountain",
                        "q1_style", "q2_atmosphere", "pref_nature", "pref_culture", "pref_art",
                        "pref_welness", "pref_food_local", "pref_food_style", "pref_accom_type",
                        "pref_word", "mbti", "free_request", "pref_food_style_ms", "pref_word_ms",
                        "mbti_input", "uploaded_image_files", "defaults_loaded"
                    ]
                    for k in keys_clr:
                        if k in st.session_state:
                            del st.session_state[k]
                    st.session_state.current_question_step = 1
                    st.session_state.defaults_loaded = False # デフォルト読み込みもリセット
                    st.rerun()

            # --- デフォルト値読み込み完了後 かつ しおり生成前: 質問ステップ表示 ---
            elif st.session_state.defaults_loaded:
                step = st.session_state.current_question_step
                # TOTAL_QUESTION_STEPS は質問総数 (要定義)
                st.progress(step / TOTAL_QUESTION_STEPS)

                # question_definitions は質問定義リスト (要定義)
                current_q = next((q for q in question_definitions if q["step"] == step), None)

                if current_q:
                    q_key = current_q["key"]
                    q_label = current_q["label"]
                    q_type = current_q["type"]
                    q_opts = current_q.get("options")
                    q_help = current_q.get("help")
                    # デフォルト値は読み込み済みのセッションステートから取得
                    q_def_val = st.session_state.get(q_key)
                    q_min = current_q.get("min")
                    q_max = current_q.get("max")
                    q_key_suf = current_q.get("key_suffix", "")
                    q_f_types = current_q.get("file_types")

                    st.subheader(f"Step {step}/{TOTAL_QUESTION_STEPS}: {q_label}")

                    input_widget = None
                    widget_key = f"widget_{q_key}{q_key_suf}"

                    # --- ウィジェット表示 ---
                    if q_type == "button_choice":
                        cols = st.columns(len(q_opts))
                        for i, opt in enumerate(q_opts):
                            with cols[i]:
                                st.markdown('<div class="choice-button">', unsafe_allow_html=True)
                                if st.button(opt, key=f"btn_{q_key}_{opt}"):
                                    st.session_state[q_key] = opt
                                    st.session_state.current_question_step += 1
                                    st.rerun()
                                st.markdown('</div>', unsafe_allow_html=True)

                    elif q_type == "text_area":
                        val_disp = q_def_val if q_def_val is not None else ""
                        input_widget = st.text_area("", value=val_disp, help=q_help, key=widget_key)

                    elif q_type == "number_input":
                        # number_input のデフォルト値は数値型であることを保証
                        default_num = q_def_val if isinstance(q_def_val, (int, float)) else current_q.get("default")
                        val_disp = default_num if isinstance(default_num, (int, float)) else (q_min if q_min is not None else 0)
                        input_widget = st.number_input("", min_value=q_min, max_value=q_max, value=val_disp, step=1, key=widget_key, help=q_help)

                    elif q_type == "slider":
                        default_slider = q_def_val if isinstance(q_def_val, (int, float)) else current_q.get("default")
                        val_disp = default_slider if isinstance(default_slider, (int, float)) else (q_min if q_min is not None else 0)
                        input_widget = st.slider("", min_value=q_min, max_value=q_max, value=val_disp, key=widget_key, help=q_help)

                    elif q_type == "multiselect":
                        default_list = q_def_val if isinstance(q_def_val, list) else []
                        # 選択肢に存在するデフォルト値のみを設定
                        valid_defs = [v for v in default_list if v in q_opts]
                        input_widget = st.multiselect("", options=q_opts, default=valid_defs, key=widget_key, help=q_help)

                    elif q_type == "text_input":
                        val_disp = q_def_val if q_def_val is not None else ""
                        input_widget = st.text_input("", value=val_disp, key=widget_key, help=q_help)

                    elif q_type == "file_uploader":
                        files_widget = st.file_uploader("", type=q_f_types, accept_multiple_files=True, key=widget_key, help=q_help)
                        if files_widget:
                            input_widget = files_widget[:3] # 3枚まで
                            if len(files_widget) > 3:
                                st.warning("画像は3枚までです")
                        else:
                            input_widget = []

                    # --- 「次へ」または「生成」ボタン (button_choice以外) ---
                    if q_type != "button_choice":
                        if step < TOTAL_QUESTION_STEPS:
                            st.markdown('<div class="next-step-button-wrapper">', unsafe_allow_html=True)
                            st.markdown('<div class="next-step-button">', unsafe_allow_html=True)
                            if st.button("次へ", key=f"next_{step}"):
                                st.session_state[q_key] = input_widget
                                valid = True # 必要に応じてバリデーションを追加
                                if valid:
                                    st.session_state.current_question_step += 1
                                    st.rerun()
                            st.markdown('</div>', unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                        else: # 最終ステップ
                            st.markdown('<div class="generate-button-wrapper">', unsafe_allow_html=True)
                            st.markdown('<div class="generate-button">', unsafe_allow_html=True)
                            if st.button("好みを確定して旅のしおりを生成✨", key="generate_itinerary"):
                                st.session_state[q_key] = input_widget
                                # --- しおり生成処理 ---
                                with st.spinner(f"{st.session_state.planner['name']}がしおり作成中..."):
                                    try:
                                        # --- 1. 行き先決定 ---
                                        q_keys_dest = ["q0_sea_mountain", "q1_style", "q2_atmosphere"]
                                        # ★ map_prefs は実際の都道府県リストで定義してください ★
                                        map_prefs = {
                                         "q0_sea_mountain": {
                                             "海": ["茨城県", "千葉県", "神奈川県", "静岡県", "愛知県", "三重県", "徳島県", "香川県", "高知県", "福岡県", "佐賀県", "沖縄県", "和歌山県", "兵庫県", "岡山県", "広島県", "山口県", "愛媛県", "大分県", "宮崎県", "鹿児島県", "長崎県", "熊本県", "福井県", "石川県", "富山県", "新潟県", "東京都", "宮城県", "岩手県", "青森県", "北海道"],
                                             "山": ["山形県", "栃木県", "群馬県", "山梨県", "長野県", "岐阜県", "滋賀県", "奈良県", "埼玉県", "福島県", "秋田県"],
                                             "どちらでも": st.session_state.all_prefectures # 全都道府県リスト
                                         },
                                         "q1_style": {
                                             "アクティブに観光": ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "大阪府", "兵庫県", "広島県", "福岡県", "熊本県", "沖縄県"],
                                             "ゆったり過ごす": ["山梨県", "滋賀県", "京都府", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "佐賀県", "長崎県", "大分県", "宮崎県", "鹿児島県", "沖縄県", "北海道", "青森県", "秋田県", "岩手県", "山形県", "福島県", "群馬県", "栃木県", "長野県", "岐阜県", "石川県", "富山県", "三重県", "和歌山県"]
                                             # 注: 元の詳細定義に q1_style の "どちらでも" が無いため、ここにも含めていません。
                                             # もしアプリの質問肢に "どちらでも" がある場合は、"どちらでも": st.session_state.all_prefectures を追加してください。
                                         },
                                         "q2_atmosphere": {
                                             "和の雰囲気": ["青森県", "岩手県", "秋田県", "山形県", "福島県", "栃木県", "群馬県", "新潟県", "富山県", "石川県", "福井県", "岐阜県", "三重県", "滋賀県", "京都府", "奈良県", "和歌山県", "鳥取県", "島根県", "山口県", "徳島県", "愛媛県", "佐賀県", "長崎県", "熊本県", "大分県", "鹿児島県", "岡山県", "広島県", "香川県", "高知県"],
                                             "モダン・都会的": ["北海道", "宮城県", "埼玉県", "千葉県", "東京都", "神奈川県", "静岡県", "愛知県", "京都府", "大阪府", "兵庫県", "広島県", "福岡県"],
                                             "こだわらない": st.session_state.all_prefectures # 全都道府県リスト
                                         }
                                     }
                                        cands = set(st.session_state.all_prefectures)
                                        all_q_ans = True
                                        for qk in q_keys_dest:
                                            ans = st.session_state.get(qk)
                                            if ans is None:
                                                st.warning(f"質問未回答 ({qk})。ランダムな行き先になります。")
                                                all_q_ans = False
                                                # break # 未回答で停止する場合はコメント解除
                                            elif ans in map_prefs.get(qk, {}):
                                                prefs_for_ans = map_prefs[qk].get(ans, st.session_state.all_prefectures)
                                                cands.intersection_update(set(prefs_for_ans))

                                        # if not all_q_ans: st.stop() # 未回答で停止する場合

                                        if not cands:
                                            st.warning("条件合致都道府県なし。ランダムに選びます。")
                                            cands = set(st.session_state.all_prefectures)
                                            if not cands: st.error("都道府県リスト未設定"); st.stop()

                                        dest_int = random.choice(list(cands))
                                        st.session_state.determined_destination_for_prompt = dest_int
                                        st.session_state.dest = dest_int
                                        print(f"Dest determined: {dest_int}")

                                        # --- 2. プロンプト情報収集 ---
                                        prefs_prompt = {}
                                        # PREF_KEY_MAP は {'プロンプトキー': 'session_stateキー'} の辞書 (要定義)
                                        for pk, sk in PREF_KEY_MAP.items():
                                            v = st.session_state.get(sk)
                                            if v is not None and v != [] and v != "":
                                                prefs_prompt[pk] = v
                                        st.session_state.preferences_for_prompt = prefs_prompt
                                        print(f"Prefs for prompt:\n{json.dumps(prefs_prompt, indent=2, ensure_ascii=False)}")

                                        # --- 3. プロンプト作成 ---
                                        if not st.session_state.planner:
                                            st.error("プランナー未選択")
                                            st.stop()

                                        nav_pers = st.session_state.planner.get("prompt_persona", "プロ旅行プランナーとして")
                                        days = st.session_state.get("days", 1)
                                        food_list = prefs_prompt.get('料理ジャンル', [])
                                        food_ex = food_list[0] if food_list else "食事"
                                        word_list = prefs_prompt.get('気になるワード', [])
                                        word_ex = word_list[0] if word_list else '観光'

                                        # プロンプト本文 (前のQ&Aのものを流用)
                                        prompt = f"""
あなたは旅のプランナー「Okosy」です。ユーザーの入力情報をもとに、SNS映えや定番から少し離れた、ユーザー自身の感性に寄り添うような、パーソナルな旅のしおりを作成してください。
**ユーザーに最高の旅体験をデザインすることを最優先としてください。**
**【重要】ユーザーは具体的で最新の場所情報を求めています。そのため、以下の指示に従って必ず `search_google_places` ツールを使用してください。**

【基本情報】
- 行き先: {dest_int}
- 旅行日数: {days}日

【ユーザーの好み・要望】
{json.dumps(prefs_prompt, ensure_ascii=False, indent=2)}
★★★ 上記の好み（特に「自然」「歴史文化」「アート」「ウェルネス」の度合い、「気になるワード」、「MBTI（もしあれば）」、「自由記述」）や、ユーザーがアップロードした好みの画像（もしあれば、画像ラベルとして後述）も考慮して、雰囲気や場所選びの参考にしてください。★★★

【出力指示】
1.  **構成:** 冒頭に、{st.session_state.planner['name']}として、なぜこの目的地({dest_int})を選んだのか、どんな旅になりそうか、全体の総括を **{nav_pers}** 言葉で語ってください。その後、{days}日間の旅程を、各日ごとに「午前」「午後」「夜」のセクションに分けて提案してください。時間的な流れが自然になるようにプランを組んでください。

2.  **内容:**
    * なぜその場所や過ごし方がユーザーの好みに合っているか、**{nav_pers}言葉**で理由や提案コメントを添えてください。「気になるワード」や「自由記述」の要望を意識的にプランに盛り込んでください。MBTIタイプも性格傾向を考慮するヒントにしてください。画像から読み取れた特徴も踏まえてください。
    * 隠れ家/定番のバランスはユーザーの好みに合わせてください。
    * 食事や宿泊の好みも反映してください。
    * **【説明の詳細度】** 各場所や体験について、情景が目に浮かぶような、**{nav_pers}として感情豊かに、魅力的で詳細な説明**を心がけてください。単なるリストアップではなく、そこで感じられるであろう雰囲気や感情、おすすめのポイントなどを描写してください。ユーザーの好みを反映した説明をお願いします。

3.  **【場所検索の実行 - 必須】** 以下の4種類の場所について、それぞれ **必ず `search_google_places` ツールを呼び出して** 最新の情報を取得してください。取得した情報は行程提案に **必ず** 反映させる必要があります。
    * **① 昼食:** `place_type`を 'restaurant' または 'cafe' として、ユーザーの好みに合う昼食場所を検索してください。（クエリ例: "{dest_int} ランチ {prefs_prompt.get('気になるワード', ['おしゃれ'])[0]}"）**ツール呼び出しを実行してください。**
    * **② 夕食:** `place_type`を 'restaurant' として、ユーザーの好みに合う夕食場所を検索してください。（クエリ例: "{dest_int} ディナー {food_ex} 人気"）**ツール呼び出しを実行してください。**
    * **③ 宿泊:** `place_type`を 'lodging' として、ユーザーの宿泊タイプや好みに合う宿泊施設を検索してください。（クエリ例: "{dest_int} {prefs_prompt.get('宿タイプ','宿')} {prefs_prompt.get('気になるワード', ['温泉', '静か'])[0]}"）**ツール呼び出しを実行してください。**
    * **④ 観光地:** `place_type`を 'tourist_attraction', 'museum', 'park', 'art_gallery' 等からユーザーの好みに合うものを選択し、関連する観光スポットを検索してください。（クエリ例: "{dest_int} {word_ex} スポット"）**ツール呼び出しを実行してください。**

4.  **【検索結果の利用と表示】**
    * `search_google_places` ツールで得られた場所を提案に含める際は、その場所名にGoogle Mapsへのリンクを **Markdown形式** で付与してください。**リンクのURLは `https://www.google.com/maps/place/?q=place_id:<PLACE_ID>` の形式**とし、`<PLACE_ID>` はツールの結果に含まれる `place_id` を使用してください。例: `[レストラン名](https://www.google.com/maps/place/?q=place_id:ChIJ)`
    * **【重要】** 場所名は**Markdownリンクの中にのみ**含めてください。リンクの前後で場所名を繰り返さないでください。
    * デバック表示で出てくるお店に関しても、同じように場所名に対してリンクが着くようしてください(マップコードは出力不要です)
    * **各日の夜のパートには、ステップ③のツール検索結果から**、**必ず**最適な宿泊施設を1つ選び、その名前と上記形式のGoogle Mapsリンクを記載してください。検索結果がない場合や検索しなかった場合でも、一般的な宿泊エリアやタイプの提案をしてください。
    * 初日は必ず午前から始め、ホテルは出さないでください。最終日は夜の情報を出力せず午後で帰るようにしてください。
    * ツール検索でエラーが出たり、場所が見つからなかったりした場合は、無理に場所名を記載せず、その旨を行程中に記載してください。

5.  **形式:** 全体を読みやすい**Markdown形式**で出力してください。各日の区切り（例: `--- 1日目 ---`）、午前/午後/夜のセクション（例: `**午前:**`）などを明確にしてください。

{st.session_state.planner['name']}として、ユーザーに最高の旅体験をデザインしてください。
"""
                                        st.session_state.messages_for_prompt = [{"role": "user", "content": prompt}]

                                        # --- 4. API呼び出し ---
                                        # run_conversation_with_function_calling はLLM APIと通信する関数 (要定義)
                                        final_res, places_res_json = run_conversation_with_function_calling(
                                            st.session_state.messages_for_prompt,
                                            st.session_state.get("uploaded_image_files", [])
                                        )

                                        # --- 5. 結果表示 ---
                                        if final_res and "申し訳ありません" not in final_res:
                                            st.session_state.itinerary_generated = True
                                            st.session_state.generated_shiori_content = final_res
                                            st.session_state.final_places_data = places_res_json
                                            st.success("しおり完成！")
                                            st.balloons()
                                            st.rerun()
                                        else:
                                            st.error("しおり生成エラー")
                                            print(f"AI Res Err: {final_res}")
                                            st.session_state.itinerary_generated = False
                                    except Exception as gen_e:
                                         st.error(f"しおり生成中に予期せぬエラー: {gen_e}")
                                         st.session_state.itinerary_generated = False

                            st.markdown('</div>', unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                # 現在の質問ステップが予期せぬ値の場合
                elif step > TOTAL_QUESTION_STEPS:
                    st.warning("予期せぬ状態です。最初のステップに戻ります。")
                    st.session_state.current_question_step = 1 # または 0
                    st.session_state.defaults_loaded = False
                    st.rerun()
                # current_q が見つからない場合 (通常発生しないはず)
                else:
                     st.warning("現在の質問が見つかりません。")
            # デフォルト値読み込み中の表示は spinner が担当するので else は不要


    # --- 8. 過去の旅のしおりを見る ---
    elif menu_choice == "過去の旅のしおりを見る":
        st.header("過去の旅のしおり")

        if not user_id:
            st.error("ユーザー情報未取得")
            st.stop()

        # Firestoreからしおりリストを読み込み (要定義)
        itins = load_itineraries_from_firestore(user_id)

        if not itins:
            st.info("保存しおりなし")
        else:
            st.write(f"{len(itins)}件のしおりあり")

            # しおり選択のドロップダウン用オプション作成
            itin_opts = {}
            for i in itins:
                name = i.get('name', '名称未設定')
                date_str = "日付不明"
                cdt = i.get('creation_date')
                if isinstance(cdt, datetime.datetime):
                     if cdt.tzinfo:
                         cdt_jst = cdt.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
                         date_str = cdt_jst.strftime('%y/%m/%d %H:%M')
                     else:
                         date_str = cdt.strftime('%y/%m/%d %H:%M') + " (UTC?)"
                elif cdt:
                    date_str = str(cdt)
                itin_opts[i['id']] = f"{name} ({date_str})"

            # しおり選択
            sel_id = st.selectbox(
                "表示/編集/削除したいしおり選択",
                options=list(itin_opts.keys()),
                format_func=lambda x: itin_opts.get(x, "不明なしおり"),
                index=None,
                key="sel_itin_id_sel"
            )
            st.session_state.selected_itinerary_id = sel_id

            # しおりが選択された場合
            if st.session_state.selected_itinerary_id:
                sel_itin = next((i for i in itins if i["id"] == st.session_state.selected_itinerary_id), None)

                if sel_itin:
                    st.subheader(f"しおり: {sel_itin.get('name', '名称未設定')}")

                    # 作成日時表示
                    cdt_utc = sel_itin.get('creation_date')
                    if cdt_utc and isinstance(cdt_utc, datetime.datetime):
                        if cdt_utc.tzinfo:
                            cdt_loc = cdt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
                            st.caption(f"作成日時: {cdt_loc.strftime('%Y-%m-%d %H:%M')} JST")
                        else:
                            st.caption(f"作成日時: {cdt_utc.strftime('%Y-%m-%d %H:%M')} (UTC?)")
                    elif cdt_utc:
                        st.caption(f"作成日時: {str(cdt_utc)}")
                    else:
                        st.caption("作成日時不明")

                    # 保存された好み情報表示
                    with st.expander("▼ このしおりを作成した時の好み", expanded=False):
                        prefs_d = sel_itin.get('preferences_dict', {})
                        if prefs_d:
                            st.json(prefs_d)
                        else:
                            st.info("保存好み情報なし")

                    # しおり本文表示
                    st.markdown(sel_itin.get("generated_content", "コンテンツなし"))
                    st.markdown("---")

                    # 保存場所データ表示 (デバッグ用)
                    with st.expander("▼ 保存場所データ (デバッグ用)"):
                        data_str_past = sel_itin.get("places_data")
                        if data_str_past:
                            try:
                                res_list_past = json.loads(data_str_past)
                                titles_past = ["①昼食","②夕食","③宿泊","④観光"]
                                if isinstance(res_list_past, list):
                                    for i, res_data_past in enumerate(res_list_past):
                                        title_past = titles_past[i] if i < len(titles_past) else f"Tool{i+1}"
                                        st.subheader(title_past)
                                        places_past = None
                                        try:
                                            if isinstance(res_data_past, str):
                                                places_past = json.loads(res_data_past)
                                            elif isinstance(res_data_past, (list, dict)):
                                                places_past = res_data_past
                                            else:
                                                # --- 不正な形式の場合 ---
                                                st.warning(f"不正形式:{type(res_data_past)}")
                                                st.text(str(res_data_past))
                                                # ★★★ 修正点: continue を elseブロックの最後に配置 ★★★
                                                continue
                                        # --- ★★★ 修正点: except ブロックを追加 ★★★ ---
                                        except json.JSONDecodeError as json_e:
                                            st.error(f"JSONデコード失敗:{json_e}")
                                            st.text(str(res_data_past))
                                            # エラー時も次のループへ
                                            continue
                                        except Exception as e:
                                            st.error(f"場所データ表示エラー:{e}")
                                            st.text(str(res_data_past))
                                            # エラー時も次のループへ
                                            continue

                                        # places_past が正常に取得できた場合のみ表示
                                        if places_past is not None:
                                            if isinstance(places_past, list):
                                                if places_past:
                                                    try:
                                                        df_past = pd.DataFrame(places_past)
                                                        if 'place_id' in df_past.columns and 'name' in df_past.columns:
                                                            df_past['Map'] = df_past.apply(lambda r: f"[{r['name']}](https://www.google.com/maps/place/?q=place_id:{r['place_id']})" if pd.notna(r.get('place_id')) and r.get('name') else r.get('name',''), axis=1)
                                                            cols_past=["name","rating","address","Map"]
                                                        else:
                                                            st.warning("place_id欠損")
                                                            df_past['Map'] = df_past['name']
                                                            cols_past=["name","rating","address"]
                                                        df_disp_past = df_past[[c for c in cols_past if c in df_past.columns]]
                                                        html_past = df_disp_past.to_html(escape=False, index=False, na_rep="-", justify="left")
                                                        st.markdown(html_past, unsafe_allow_html=True)
                                                    except Exception as df_e:
                                                        st.error(f"DF表示エラー:{df_e}")
                                                        st.json(places_past)
                                                else:
                                                    st.info("場所データ空")
                                            elif isinstance(places_past, dict):
                                                if "error" in places_past:
                                                    st.error(f"エラー:{places_past['error']}")
                                                elif "message" in places_past:
                                                    st.info(places_past['message'])
                                                else:
                                                    st.json(places_past)
                                            else:
                                                st.warning(f"不正データ形式:{type(places_past)}")
                                                st.text(str(places_past))
                                else:
                                    st.warning("場所データ形式不正(リストでない)")
                                    st.text(data_str_past)
                            except json.JSONDecodeError:
                                st.error("場所データ全体JSONデコード失敗")
                                st.text(data_str_past)
                            except Exception as e:
                                st.error(f"場所データ処理エラー:{e}")
                                st.text(data_str_past)
                        else:
                            st.info("保存場所データなし")

                    st.markdown("---")

                    # 思い出投稿フォーム
                    st.subheader("✈️ 旅の思い出を追加")
                    if sel_itin and 'id' in sel_itin:
                        with st.form(f"mem_form_{sel_itin['id']}", clear_on_submit=True):
                            mem_cap = st.text_area("キャプション", key=f"mem_cap_{sel_itin['id']}")
                            mem_pho = st.file_uploader("写真(任意)", type=["jpg","jpeg","png"], key=f"mem_pho_{sel_itin['id']}")
                            submit_mem = st.form_submit_button("思い出投稿")

                            if submit_mem:
                                if mem_cap or mem_pho:
                                    pho_b64 = None
                                    if mem_pho:
                                        try:
                                            img_b = mem_pho.getvalue()
                                            pho_b64 = base64.b64encode(img_b).decode('utf-8')
                                        except Exception as img_e:
                                            st.warning(f"写真処理エラー:{img_e}")
                                    # Firestoreへの保存関数 (要定義)
                                    saved_mid = save_memory_to_firestore(user_id, sel_itin['id'], mem_cap, pho_b64)
                                    if saved_mid:
                                        st.success("思い出投稿成功！")
                                        st.rerun()
                                    else:
                                        st.error("思い出投稿失敗")
                                else:
                                    st.warning("キャプションか写真入力要")
                    else:
                         st.warning("しおりが選択されていません。")


                    st.markdown("---")

                    # 思い出アルバム表示
                    st.subheader("📖 思い出アルバム")
                    if sel_itin and 'id' in sel_itin:
                        # Firestoreから思い出を読み込み (要定義)
                        mems = load_memories_from_firestore(user_id, sel_itin['id'])
                        if not mems:
                            st.info("思い出投稿なし")
                        else:
                            cols = st.columns(3)
                            col_idx = 0
                            for mem in mems:
                                with cols[col_idx % 3]:
                                    st.markdown(f"**{mem.get('caption', '(キャプション無)')}**")
                                    # 日付表示
                                    mcdt_utc = mem.get('creation_date')
                                    if mcdt_utc and isinstance(mcdt_utc, datetime.datetime):
                                        if mcdt_utc.tzinfo:
                                            mcdt_loc = mcdt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
                                            st.caption(f"{mcdt_loc.strftime('%y/%m/%d %H:%M')}")
                                        else:
                                            st.caption(f"{mcdt_utc.strftime('%Y-%m-%d %H:%M')} (UTC?)")
                                    elif mcdt_utc:
                                         st.caption(str(mcdt_utc))
                                    # 写真表示
                                    pho_img_obj = mem.get('photo_image') # 修正: photo_imageキーを使う
                                    if pho_img_obj:
                                        try:
                                            # すでにImageオブジェクトなのでそのまま表示
                                            st.image(pho_img_obj, use_column_width=True)
                                        except Exception as display_e:
                                            st.warning(f"画像表示エラー: {display_e}")

                                    # 削除ボタン
                                    mem_id_to_delete = mem.get('id')
                                    if mem_id_to_delete: # IDがないと削除できない
                                         if st.button("削除", key=f"del_mem_{mem_id_to_delete}", help="この思い出削除"):
                                             # Firestoreからの削除関数 (要定義)
                                             if delete_memory_from_firestore(user_id, sel_itin['id'], mem_id_to_delete):
                                                 st.success("思い出削除成功")
                                                 st.rerun()
                                             else:
                                                 st.error("思い出削除失敗")
                                    st.markdown("---") # 思い出ごとの区切り
                                col_idx += 1
                    else:
                        st.warning("しおりが選択されていません。")

                    st.markdown("---")

                    # しおり削除ボタン
                    if sel_itin and 'id' in sel_itin:
                        st.error("⚠️ このしおりを削除する")
                        if st.button("削除実行(元に戻せません)", key=f"del_itin_{sel_itin['id']}", type="secondary", help="しおりと思い出全て削除されます。"):
                            # Firestoreからの削除関数 (要定義)
                            if delete_itinerary_from_firestore(user_id, sel_itin['id']):
                                st.success(f"しおり「{sel_itin.get('name','名称未設定')}」削除成功")
                                st.session_state.selected_itinerary_id = None
                                if 'sel_itin_id_sel' in st.session_state:
                                    st.session_state.sel_itin_id_sel = None
                                st.rerun()
                            else:
                                st.error("しおり削除失敗")

                # sel_itin が見つからなかった場合
                else:
                    st.warning("選択されたしおりデータが見つかりません。")
                    st.session_state.selected_itinerary_id = None
                    if 'sel_itin_id_sel' in st.session_state:
                        st.session_state.sel_itin_id_sel = None
                    # st.rerun() # 必要なら再実行

# --- フッター --- (この部分は元のインデントレベルのまま)
st.sidebar.markdown("---")
st.sidebar.info("Okosy v1.6.0 (入力形式変更版)")