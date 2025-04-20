# -*- coding: utf-8 -*-
import streamlit as st

# ============================================================
#  ヘルパー: 都道府県名を正規化（末尾の都/道/府/県を取り除く）
# ============================================================
def normalize_pref_name(pref: str) -> str:
    """'東京都'→'東京', '北海道'→'北海', '大阪府'→'大阪' のように末尾を除いて比較用に返す"""
    return pref.replace("県", "").replace("府", "").replace("都", "").replace("道", "")


st.markdown("""
<style>
    /* ページ全体のコンテナ調整 */
    .block-container {
        padding-top: 1rem;
    }

    /* 中央揃えのタイトル */
    .title-center {
        text-align: center;
        font-size: 40px;
        font-weight: 700;
        color: #246798; /* Okosyカラー */
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    /* ボタンラッパー */
    .button-wrapper, .center-button-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
        margin-bottom: 60px;
    }

    /* --- Streamlit 標準ボタン --- */
    /* 全てのボタンに共通する基本スタイル */
    div[data-testid="stButton"] > button {
        padding: 0.75em 2.5em;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        transition: transform 0.2s ease, background-color 0.4s ease, color 0.4s ease, border-color 0.4s ease;
        width: auto;
        display: inline-block;
        cursor: pointer;
        /* ★★★ 枠線の太さを維持 ★★★ */
        border: 1.5pt solid; /* 太さだけ指定 */
    }

    /* 非選択時 (secondary or default) */
    /* kind="secondary" と kind指定なしの両方を対象 */
    div[data-testid="stButton"] > button:where([kind="secondary"]),
    div[data-testid="stButton"] > button:not(:where([kind="primary"])) {
        background-color: transparent !important;
        color: #246798 !important;
        border-color: #246798 !important; /* 枠線は青 */
    }

    /* 選択時 (primary) - これは特定のUIのためのカスタムスタイルなので残します */
    div[data-testid="stButton"] > button:where([kind="primary"]) {
        background-color: #EAEAEA !important; /* 背景: 灰色 */
        color: #333333 !important; /* 文字: 濃い灰色 */
        /* 枠線を薄いグレーに */
        border-color: #CCCCCC !important;
    }

    /* ホバー時 (非選択ボタン) */
    div[data-testid="stButton"] > button:where([kind="secondary"]):hover,
    div[data-testid="stButton"] > button:not(:where([kind="primary"])):hover {
        background-color: #DDDDDD !important;  /* 背景: 少し濃いグレー */
        color: #555555 !important; /* 文字: グレー */
        /* ホバー時も枠線を維持（非選択時と同じ青） */
        border-color: #246798 !important;
        transform: scale(1.05);
    }

    /* ホバー時 (選択済みボタン) */
    div[data-testid="stButton"] > button:where([kind="primary"]):hover {
        background-color: #D0D0D0 !important; /* 背景: さらに濃いグレー */
        color: #333333 !important; /* 文字: 濃い灰色 */
        /* 選択時ホバーも枠線を維持（選択時と同じ薄いグレー） */
        border-color: #CCCCCC !important;
        transform: scale(1.05);
    }
            


    /* --- 特定ボタンのラッパー調整 --- */
    .planner-button > div[data-testid="stButton"] > button { width: 100%; margin-bottom: 10px; }
    
    .next-step-button > div[data-testid="stButton"] > button { /* スタイル継承 */ }
    .generate-button > div[data-testid="stButton"] > button { background-color: #246798; color: white; border: none; padding: 1em 3em; font-size: 22px; font-weight: bold; border-radius: 12px; }
    .generate-button > div[data-testid="stButton"] > button:hover { background-color: #1E537A; color: white; transform: scale(1.05); border: none; }

    /* --- Streamlit 標準ウィジェット調整 --- */

    /* ラベル共通 */
    .stSlider > label,
    .stMultiSelect > label,
    .stTextArea > label,
    .stTextInput > label,
    .stFileUploader > label,
    .stNumberInput > label,
    div[data-testid="stRadio"] label {
        font-weight: bold;
        margin-bottom: 5px;
        color: #31333F !important; /* 標準テキスト色 (theme.textColorで設定可能だが、個別指定を残す場合) */
    }

    /* ラジオボタン */
    div[data-testid="stRadio"] > div[role="radiogroup"] { justify-content: flex-start !important; gap: 15px; } /* レイアウト調整は残す */
    .stRadio > div > div { justify-content: flex-start !important; } /* レイアウト調整は残す */
    div[data-testid="stRadio"] label span { color: #31333F !important; } /* ラベル文字色 */
    div[data-testid="stRadio"] input[type="radio"] + div::before { /* 非選択時の円 */
        border-color: #CCCCCC !important; /* 非選択時のスタイルは残す */
        background-color: transparent !important;
    }
    /* ★★★ 選択時のラジオボタンの色設定 (削除) ★★★ */
    /* ★★★ フォーカス時のラジオボタンの色設定 (削除) ★★★ */


    /* スライダー */
    div[data-testid="stSlider"] div[data-baseweb="slider"] > div:nth-child(1) { /* トラック背景 */
        background-color: #E0E0E0 !important; /* 非アクティブ部分の色は残す */
    }
    /* ★★★ スライダーのアクティブなバーの色設定 (削除) ★★★ */
    /* ★★★ スライダーのハンドルの色設定 (削除) ★★★ */


    /* マルチセレクト */
    div[data-testid="stMultiSelect"] div[data-baseweb="tag"] { /* 選択済みタグ */
        background-color: #ADCDE3 !important; /* primaryColorとは違う独自スタイルなので残す */
        color: #1E537A !important;
        border: 1px solid #ADCDE3 !important;
    }
            
            /* 通常の選択肢ボタン */
    .choice-button button[data-testid^="stBaseButton"] { /* セレクタ修正 */
    width: 100%;
    margin-bottom: 10px;
    font-size: 16px;      /* 標準のフォントサイズ */
    padding: 0.8em 1.0em; /* 調整後のパディング (例) */
    /* 他に必要な共通スタイルがあればここにも記述 */
    }

/* 長いテキストを持つ選択肢ボタン */
    .long-choice-button button[data-testid^="stBaseButton"] { /* セレクタ修正 */
    width: 100%;
    margin-bottom: 10px;
    font-size: 10px;      /* ★★★ 小さいフォントサイズを指定 (9pxより少し大きく) ★★★ */
    padding: 0.8em 1.0em; /* パディングは通常ボタンと合わせる (例) */
    /* white-space: nowrap; */ /* 必要であれば */
    }



    /* テキスト入力系・ファイルアップローダの枠線・フォーカス */
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stNumberInput"] input,
    div[data-testid="stFileUploader"] section {
        border: 1px solid #CCCCCC !important; /* デフォルトの枠線は残す */
    }
    /* ★★★ フォーカス時の入力系ウィジェットの枠線・影の色設定 (削除) ★★★ */

    /* ★★★ Number Input の +/- ボタンの色設定 (削除) ★★★ */
    /* ★★★ Number Input の +/- ボタンのホバー色設定 (削除) ★★★ */

</style>
""", unsafe_allow_html=True)

# --- 1. 必要なライブラリのインポート ---
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
from collections import Counter
import statistics

# Firebase 関連ライブラリ
import firebase_admin
from firebase_admin import credentials, auth, firestore
try: import streamlit_firebase_auth as sfa
except ImportError: st.error("認証ライブラリ未検出"); sfa = None
except Exception as e: st.error(f"認証ライブラリImportエラー: {e}"); sfa = None
LONG_BUTTON_LABELS = {"夫婦・カップル", "気にしない"}

# Google Cloud Vision
try:
    from google.cloud import vision
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request
except ImportError: st.error("Visionライブラリ未検出"); vision = None; service_account = None; Request = None

# --- ヘッダー画像表示 ---
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
    try:
        # SecretsからJSON文字列を取得
        firebase_sa_json_str = st.secrets.get("FIREBASE_SERVICE_ACCOUNT_JSON")
        if not firebase_sa_json_str:
            st.error("Firebase SAキーがSecretsに設定されていません (FIREBASE_SERVICE_ACCOUNT_JSON)")
            st.stop()
        # JSON文字列を辞書に変換
        firebase_sa_dict = json.loads(firebase_sa_json_str)
        cred = credentials.Certificate(firebase_sa_dict)
        firebase_admin.initialize_app(cred)
        print("Firebase Admin SDK initialized from Secrets.")
    except json.JSONDecodeError:
        st.error("SecretsのFirebase SAキー (JSON) の形式が正しくありません。")
        st.stop()
    except Exception as e:
        st.error(f"Firebase Admin SDK 初期化失敗 (Secrets): {e}")
        st.error(traceback.format_exc())
        st.stop()
# --- 2.1 Firebase Web アプリ設定の読み込み ---
# <<< 全文: Firebase Web設定読み込み (Secrets対応) >>>
firebase_config = None
try:
    # SecretsからJSON文字列を取得
    firebase_config_json_str = st.secrets.get("FIREBASE_CONFIG_JSON")
    if not firebase_config_json_str:
        st.error("Firebase Web設定がSecretsに設定されていません (FIREBASE_CONFIG_JSON)")
        st.stop()
    # JSON文字列を辞書に変換
    firebase_config = json.loads(firebase_config_json_str)
    print("Firebase Web config loaded from Secrets.")
except json.JSONDecodeError:
    st.error("SecretsのFirebase Web設定 (JSON) の形式が正しくありません。")
    st.stop()
except Exception as e:
    st.error(f"Firebase Web 設定読込失敗 (Secrets): {e}")
    st.stop()
    
# --- 2.2 streamlit-firebase-auth コンポーネントの初期化 ---
auth_obj = None
if sfa is None: st.error("認証機能初期化失敗 (sfa is None)"); st.stop()
if firebase_config is None: st.error("Firebase Web設定未読込"); st.stop()
try: auth_obj = sfa.FirebaseAuth(firebase_config)
except Exception as e: st.error(f"FirebaseAuth オブジェクト作成失敗: {e}"); st.error(traceback.format_exc()); st.stop()

# --- 2.3 Firestore クライアントの初期化 ---
try: db = firestore.client(); print("Firestore client initialized.")
except Exception as e: st.error(f"Firestore クライアント初期化失敗: {e}"); st.error(traceback.format_exc()); st.stop()

# --- Firestore データ操作関数 ---
def save_itinerary_to_firestore(user_id: str, name: str, preferences: dict, generated_content: str, places_data: Optional[str], nickname: Optional[str] = None):
    """しおりデータをFirestoreに保存する"""
    if not db: st.error("Firestoreクライアント未初期化"); return None
    try:
        doc_ref = db.collection("users").document(user_id).collection("itineraries").document()
        data_to_save = {
            "name": name,
            "preferences": json.dumps(preferences, ensure_ascii=False),
            "generated_content": generated_content,
            "places_data": places_data if places_data else None,
            "creation_date": firestore.SERVER_TIMESTAMP # type: ignore
        }
        if nickname: data_to_save["nickname"] = nickname
        doc_ref.set(data_to_save)
        print(f"Itinerary saved: {user_id}, {doc_ref.id}"); return doc_ref.id
    except Exception as e: st.error(f"Firestore保存エラー: {e}"); print(traceback.format_exc()); return None

def load_itineraries_from_firestore(user_id: str):
    """指定したユーザーのしおり一覧をFirestoreから読み込む (最新20件)"""
    if not db: return []
    itineraries = []
    try:
        itineraries_ref = db.collection("users").document(user_id).collection("itineraries").order_by(
            "creation_date", direction=firestore.Query.DESCENDING # type: ignore
        ).limit(20).stream()
        for doc in itineraries_ref:
            data = doc.to_dict()
            if data:
                data['id'] = doc.id
                try: data['preferences_dict'] = json.loads(data.get('preferences', '{}'))
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

PREF_KEY_MAP = {
        "ニックネーム": "nickname",
        "同行者": "comp", "旅行日数": "days", "予算感": "budg", "海山": "q0_sea_mountain", "スタイル": "q1_style", "雰囲気": "q2_atmosphere",
        "自然": "pref_nature", "歴史文化": "pref_culture", "アート": "pref_art", "ウェルネス": "pref_welness", "食事場所": "pref_food_local",
        "料理ジャンル": "pref_food_style", "宿タイプ": "pref_accom_type", "気になるワード": "pref_word", "MBTI": "mbti", "自由記述": "free_request",
        "行き先": "dest"
    }

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
                    # PREF_KEY_MAP を使って、Firestoreのキー ('同行者' など) を Session State のキー ('comp' など) に対応させる
                    pref_key_in_dict = next((k for k, v in PREF_KEY_MAP.items() if v == q_key), None)
                    if pref_key_in_dict and pref_key_in_dict in prefs_dict:
                        value = prefs_dict[pref_key_in_dict]
                        if value is not None: past_prefs[q_key].append(value)

    for q_def in question_definitions:
        q_key = q_def["key"]; q_type = q_def["type"]; values = past_prefs.get(q_key, [])
        if not values: continue
        default_value = None
        try:
            if q_type in ["button_choice", "radio"]:
                if values: default_value = Counter(values).most_common(1)[0][0]
            elif q_type == "number_input" or q_type == "slider":
                numeric_values = [v for v in values if isinstance(v, (int, float))]
                if numeric_values:
                    default_value = round(statistics.mean(numeric_values))
                    if "min" in q_def and default_value < q_def["min"]: default_value = q_def["min"]
                    if "max" in q_def and default_value > q_def["max"]: default_value = q_def["max"]
            elif q_type == "multiselect":
                all_selected_items = [item for sublist in values if isinstance(sublist, list) for item in sublist]
                if all_selected_items:
                    valid_options = set(q_def.get("options", []))
                    valid_selected_items = [item for item in all_selected_items if item in valid_options]
                    if valid_selected_items: default_value = [item for item, count in Counter(valid_selected_items).most_common(3)]
            elif q_type == "text_input" or q_type == "text_area":
                if values: default_value = values[-1]
        except Exception as e: print(f"Error calc default for {q_key}: {e}"); default_value = None
        if default_value is not None:
            if q_type == "multiselect" and not isinstance(default_value, list):
                print(f"Warn: Default for multiselect {q_key} is not a list: {default_value}. Skipping.")
                continue
            if q_type in ["button_choice", "radio"] and "options" in q_def and default_value not in q_def["options"]:
                print(f"Warn: Default for {q_key} ('{default_value}') not in options {q_def['options']}. Skipping.")
                continue
            st.session_state[q_key] = default_value
            print(f"Set default for {q_key}: {default_value}")

# --- 3. 認証処理とログイン状態の管理 ---
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
if st.session_state.get('user_info') is not None:
    user_id = st.session_state['user_info'].get('uid')
    if not user_id: st.error("ユーザーID取得不可"); st.session_state['user_info'] = None; st.session_state['id_token'] = None; st.rerun()

    # --- サイドバーの設定 (ログイン後) ---
    st.sidebar.header("メニュー")
    user_email = st.session_state['user_info'].get('email', '不明')
    nickname = st.session_state.get('nickname')
    if nickname:
        st.sidebar.write(f"ログイン中: {nickname} さん ({user_email})")
    else:
        st.sidebar.write(f"ログイン中: {user_email}")
    if st.sidebar.button("ログアウト"):
        st.session_state['user_info'] = None; st.session_state['id_token'] = None
        keys_to_clear = [
            "itinerary_generated", "generated_shiori_content", "final_places_data",
            "preferences_for_prompt", "determined_destination", "determined_destination_for_prompt",
            "messages_for_prompt", "shiori_name_input", "selected_itinerary_id",
            "selected_itinerary_id_selector", "show_planner_select", "planner_selected", "planner",
            "messages", "preferences", "dest", "comp", "days", "budg",
            "pref_nature", "pref_culture", "pref_art", "pref_welness", "pref_food_local",
            "pref_food_style", "pref_accom_type", "pref_word", "mbti", "free_request",
            "pref_food_style_ms", "pref_word_ms", "mbti_input", "uploaded_image_files",
            "q0_sea_mountain", "q1_style", "q2_atmosphere", "memory_caption", "memory_photo",
            "defaults_loaded", "nickname", "current_planning_stage", "show_nickname_input"
        ]
        for key in keys_to_clear:
            if key in st.session_state: del st.session_state[key]
        st.success("ログアウトしました。"); print("User logged out.")
        time.sleep(1); st.rerun()
    st.sidebar.markdown("---")
    menu_choice = st.sidebar.radio("", ["新しい旅を計画する", "過去の旅のしおりを見る"], key="main_menu", label_visibility="collapsed")
    st.sidebar.image("assets/logo_okosy.png", width=100)

    # --- 4. Google Maps関連のヘルパー関数 ---
    def get_coordinates(address):
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
    def get_vision_labels_from_uploaded_images(image_files):
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
    def search_google_places(query: str, location_bias: Optional[str] = None, place_type: str = "tourist_attraction", min_rating: Optional[float] = 4.0, price_levels: Optional[str] = None) -> str:
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
    if "all_prefectures" not in st.session_state: st.session_state.all_prefectures = ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]

    question_definitions = [
        {"step": 1, "key": "comp", "type": "button_choice", "label": "👥 誰と行きますか？", "options": ["一人旅", "夫婦・カップル", "友人", "家族"]},
        {"step": 2, "key": "days", "type": "number_input", "label": "📅 何日間ですか？", "min": 1, "max": 30, "default": 2},
        {"step": 3, "key": "budg", "type": "button_choice", "label": "💰 予算感は？", "options": ["気にしない", "安め", "普通", "高め"], "default": "普通"},
        {"step": 4, "key": "q0_sea_mountain", "type": "radio", "label": "🌊 Q1: 海と山、どっち派？", "options": ["海", "山", "どちらでも"], "default": "どちらでも"},
        {"step": 5, "key": "q1_style", "type": "radio", "label": "🏃 Q2: 旅のスタイルは？", "options": ["アクティブに観光", "ゆったり過ごす"], "default": "アクティブに観光"},
        {"step": 6, "key": "q2_atmosphere", "type": "radio", "label": "🌸 Q3: どんな雰囲気を感じたい？", "options": ["和の雰囲気", "モダン・都会的", "こだわらない"], "default": "こだわらない"},
        {"step": 7, "key": "pref_nature", "type": "slider", "label": "🌲 自然が好き", "min": 1, "max": 5, "default": 3},
        {"step": 8, "key": "pref_culture", "type": "slider", "label": "🏯 歴史・文化が好き", "min": 1, "max": 5, "default": 3},
        {"step": 9, "key": "pref_art", "type": "slider", "label": "🎨 アートが好き", "min": 1, "max": 5, "default": 3},
        {"step": 10, "key": "pref_welness", "type": "slider", "label": "♨️ 癒やされたい (ウェルネス)", "min": 1, "max": 5, "default": 3},
        {"step": 11, "key": "pref_food_local", "type": "radio", "label": "🍽️ 食事場所の好みは？", "options": ["地元の人気店", "隠れ家的なお店", "シェフのこだわりのお店", "オーガニック・ヴィーガン対応のお店"], "default": "地元の人気店"},
        {"step": 12, "key": "pref_food_style", "type": "multiselect", "label": "🍲 好きな料理・ジャンルは？ (複数可)", "options": ["和食", "洋食", "カフェ", "スイーツ", "郷土料理", "エスニック", "中華", "イタリアン"], "key_suffix": "_ms"},
        {"step": 13, "key": "pref_accom_type", "type": "radio", "label": "🏨 泊まりたい宿のタイプは？", "options": ["ホテル", "旅館", "民宿・ゲストハウス", "こだわらない"], "default": "ホテル"},
        {"step": 14, "key": "pref_word", "type": "multiselect", "label": "✨ 気になるキーワードは？ (複数可)", "options": ["隠れた発見", "カラフル", "静かで落ち着いた", "冒険", "定番", "温泉", "寺社仏閣", "食べ歩き","ショッピング","日本酒","ワイン", "おこもり","子供と楽しむ", "ローカル体験", "アウトドア","写真映え", "パワースポット"], "key_suffix": "_ms"},
        {"step": 15, "key": "mbti", "type": "text_input", "label": "🧠 あなたのMBTIは？ (任意)", "key_suffix": "_input", "help": "例: ENFP 性格タイプに合わせて提案が変わるかも？"},
        {"step": 16, "key": "uploaded_image_files", "type": "file_uploader", "label": "🖼️ 行きたい場所のイメージに近い画像をアップロード (任意・3枚まで)", "file_types": ["jpg", "jpeg", "png"]},
        {"step": 17, "key": "free_request", "type": "text_area", "label": "📝 その他、プランナーへの要望があればどうぞ！"}
    ]

    # --- セッションステート初期化 ---
    keys_to_init = [
        ("nickname", ""), ("show_nickname_input", False),
        ("current_planning_stage", 0),
        ("show_planner_select", False),
        ("planner_selected", False),
        ("planner", None),
        ("messages", []),
        ("itinerary_generated", False),
        ("generated_shiori_content", None),
        ("final_places_data", None),
        ("preferences", {}),
        ("selected_itinerary_id", None),
        ("preferences_for_prompt", {}),
        ("determined_destination", None),
        ("determined_destination_for_prompt", None),
        ("messages_for_prompt", []),
        ("shiori_name_input", ""),
        ("selected_itinerary_id_selector", None),
        ("main_menu", "新しい旅を計画する"),
        ("defaults_loaded", False),
        ("confirmed_destination", "")
    ]
    q_keys_all = [q_def["key"] for q_def in question_definitions];
    for q_key in q_keys_all: keys_to_init.append((q_key, None))
    for key, default in keys_to_init:
        if key not in st.session_state: st.session_state[key] = default

    # --- メインコンテンツ ---
    if menu_choice == "新しい旅を計画する":
        st.markdown('<div class="title-center">さあ、あなただけの旅をはじめよう。</div>', unsafe_allow_html=True)

        # --- ステップ0: プランニング開始ボタン ---
        if not st.session_state.show_nickname_input and st.session_state.current_planning_stage == 0:
            # st.markdown('<div class="center-button-wrapper">', unsafe_allow_html=True) # ← この行を削除
            # # 3つのカラムを作成（例: 比率 1:1:1）。中央のカラム(col2)にボタンを配置
            # # 比率を調整して中央の幅を変えることも可能 (例: [2, 1, 2])
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2: # 中央のカラムにボタンを配置
                if st.button("プランニングを始める", key="start_planning_button"): # keyを追加すると良い場合がある
                    st.session_state.show_nickname_input = True
                    st.rerun()


        # --- ステップ0.5: ニックネーム入力 ---
        elif st.session_state.show_nickname_input and st.session_state.current_planning_stage == 0:
            st.subheader("まず、あなたのニックネームを教えてください")
            nickname_input = st.text_input("ニックネーム", value=st.session_state.get('nickname', ''), key="nickname_widget")
            st.markdown('<div class="next-step-button-wrapper">', unsafe_allow_html=True)
            st.markdown('<div class="next-step-button">', unsafe_allow_html=True)
            if st.button("決定", key="submit_nickname"):
                if nickname_input:
                    st.session_state.nickname = nickname_input
                    st.session_state.current_planning_stage = 1
                    st.session_state.show_nickname_input = False
                    st.session_state.defaults_loaded = False
                    st.rerun()
                else:
                    st.warning("ニックネームを入力してください。")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # --- しおり生成完了後 ---
        elif st.session_state.itinerary_generated and st.session_state.generated_shiori_content:
            st.header(f"旅のしおり （担当: {st.session_state.planner['name']}）")
            st.markdown(st.session_state.generated_shiori_content)
            st.markdown("---")

            with st.expander("▼ お店候補の表示(最大5件)", expanded=False):
                data_str = st.session_state.final_places_data
                if data_str:
                    try:
                        res_list = json.loads(data_str)
                        titles = ["①昼食", "②夕食", "③宿泊", "④観光"]
                        if isinstance(res_list, list):
                            for i, res_data in enumerate(res_list):
                                title = titles[i] if i < len(titles) else f"Tool{i+1}"
                                st.subheader(title)
                                places = None
                                try:
                                    if isinstance(res_data, str): places = json.loads(res_data)
                                    elif isinstance(res_data, (list, dict)): places = res_data
                                    else: st.warning(f"不正形式:{type(res_data)}"); st.text(str(res_data)); continue
                                except json.JSONDecodeError as json_e: st.error(f"JSONデコード失敗:{json_e}"); st.text(str(res_data)); continue
                                except Exception as e: st.error(f"場所データ表示エラー:{e}"); st.text(str(res_data)); continue

                                if places is not None:
                                    if isinstance(places, list):
                                        if places:
                                            try:
                                                df = pd.DataFrame(places)
                                                if 'place_id' in df.columns and 'name' in df.columns:
                                                    df['場所名(リンク付き)'] = df.apply(lambda r: f'<a href="https://www.google.com/maps/place/?q=place_id:{r["place_id"]}" target="_blank">{r["name"]}</a>' if pd.notna(r.get('place_id')) and pd.notna(r.get('name')) else r.get('name', ''), axis=1)
                                                    cols_to_display = ['場所名(リンク付き)', 'rating', 'address']
                                                else:
                                                    st.warning("place_idまたはname欠損のためMapリンク不可")
                                                    cols_to_display = [col for col in ['name', 'rating', 'address'] if col in df.columns]
                                                    if 'name' in cols_to_display: df.rename(columns={'name': '場所名(リンク付き)'}, inplace=True); cols_to_display[cols_to_display.index('name')] = '場所名(リンク付き)' # カラム名統一
                                                df_disp = df[[c for c in cols_to_display if c in df.columns]].copy()
                                                if 'rating' in df_disp.columns: df_disp['rating'] = df_disp['rating'].apply(lambda x: f"{x:.1f}" if pd.notna(x) and isinstance(x, (int, float)) else x)
                                                html = df_disp.to_html(escape=False, index=False, na_rep="-", justify="left")
                                                st.markdown(html, unsafe_allow_html=True)
                                            except Exception as df_e: st.error(f"DF表示エラー:{df_e}"); st.json(places)
                                        else: st.info("場所データ空")
                                    elif isinstance(places, dict):
                                        if "error" in places: st.error(f"エラー:{places['error']}")
                                        elif "message" in places: st.info(places['message'])
                                        else: st.json(places)
                                    else: st.warning(f"不正データ形式:{type(places)}"); st.text(str(places))
                        else: st.warning("場所データ形式不正(リストでない)"); st.text(data_str)
                    except json.JSONDecodeError: st.error("場所データ全体JSONデコード失敗"); st.text(data_str)
                    except Exception as e: st.error(f"場所データ処理エラー:{e}"); st.text(data_str)
                else: st.info("取得場所データなし")
            st.markdown("---")

            with st.form("save_shiori_form"):
                default_shiori_name = f"{st.session_state.get('nickname', 'あなた')}の{st.session_state.get('dest', '旅行')}のしおり"
                shiori_name = st.text_input("しおりの名前", key="shiori_name_input", value=default_shiori_name)
                if st.form_submit_button("このしおりを保存する"):
                    if shiori_name:
                        prefs_to_save = st.session_state.get('preferences_for_prompt', {}).copy()
                        prefs_to_save['行き先'] = st.session_state.get('dest')
                        prefs_to_save['ニックネーム'] = st.session_state.get('nickname')
                        if not prefs_to_save: st.warning("保存設定情報なし")
                        else:
                            saved_id = save_itinerary_to_firestore(user_id, shiori_name, prefs_to_save, st.session_state.generated_shiori_content, st.session_state.final_places_data, st.session_state.get('nickname'))
                            if saved_id: st.success(f"しおり「{shiori_name}」保存成功！")
                            else: st.error("しおり保存失敗")
                    else: st.warning("しおりの名前を入力")

            if st.button("条件を変えてやり直す"):
                keys_clr = [
                    "itinerary_generated", "generated_shiori_content", "final_places_data", "preferences_for_prompt",
                    "determined_destination", "determined_destination_for_prompt", "messages_for_prompt", "shiori_name_input",
                    "preferences", "dest", "comp", "days", "budg", "q0_sea_mountain", "q1_style", "q2_atmosphere",
                    "pref_nature", "pref_culture", "pref_art", "pref_welness", "pref_food_local", "pref_food_style",
                    "pref_accom_type", "pref_word", "mbti", "free_request", "pref_food_style_ms", "pref_word_ms",
                    "mbti_input", "uploaded_image_files", "defaults_loaded", "planner_selected", "planner",
                    "current_planning_stage", "show_nickname_input", "confirmed_destination" # confirmed_destination もクリア
                ]
                for k in keys_clr:
                    if k in st.session_state: del st.session_state[k]
                st.session_state.current_planning_stage = 1 # ステージ1からやり直し
                st.session_state.defaults_loaded = False
                st.rerun()

        # --- ニックネーム入力後 & しおり生成前: 各ステージ表示 ---
        elif st.session_state.current_planning_stage >= 1:
            # --- デフォルト値読み込み処理 ---
            if not st.session_state.defaults_loaded: # 条件をシンプルに
                with st.spinner("過去の好みを読み込み中..."):
                    load_and_set_default_preferences(user_id, question_definitions)
                    st.session_state.defaults_loaded = True

            # デフォルト値読み込み完了後に各ステージを表示
            if st.session_state.defaults_loaded:
                current_stage = st.session_state.current_planning_stage
                total_stages = 4
                st.progress(current_stage / total_stages)
                st.write(f"こんにちは、{st.session_state.nickname}さん！")

                # --- ステージ 1: プランナー選択 ---
                if current_stage == 1:
                    st.subheader(f"ステップ {current_stage}/{total_stages}: あなたにぴったりのプランナーを選んでください")
                    opts = {
                        "ベテラン": {"name": "ベテラン", "prompt_persona": "経験豊富なプロとして、端的かつ的確に", "caption": "テイスト：端的シンプル。プロ感。"},
                        "姉さん": {"name": "姉さん", "prompt_persona": "地元に詳しい世話好き姉さんとして、方言(例:関西弁/博多弁など行先による)を交えつつ元気に", "caption": "テイスト：地元方言＋親しみやすさ満点。"},
                        "ギャル": {"name": "ギャル", "prompt_persona": "最新トレンド詳しい旅好きギャルとして、絵文字(💖✨)や若者言葉多用し、テンション高めに", "caption": "テイスト：テンション高め、語尾にハート。"},
                        "王子": {"name": "王子", "prompt_persona": "あなたの旅をエスコートする王子様として、優雅で少しキザな言葉遣いで情熱的に", "caption": "テイスト：ちょっとナルシストだけど優しくリード。"}
                    }
                    c1, c2 = st.columns(2)
                    planner_selected_in_stage = False

                    current_planner_data = st.session_state.get('planner')
                    selected_planner_name = None
                    if isinstance(current_planner_data, dict):
                        selected_planner_name = current_planner_data.get('name')

                    with c1:
                        for k in ["ベテラン", "姉さん"]:
                            st.markdown('<div class="planner-button">', unsafe_allow_html=True)
                            btn_lbl = f"シゴデキ{k}" if k == "ベテラン" else f"おせっかい{k}"
                            is_selected = (selected_planner_name == opts[k]['name'])
                            button_type = "primary" if is_selected else "secondary"
                            if st.button(btn_lbl, key=f"pl_{k}", type=button_type):
                                st.session_state.planner = opts[k]
                                st.session_state.planner_selected = True
                                st.session_state.current_planning_stage = 2
                                planner_selected_in_stage = True
                            st.markdown('</div>', unsafe_allow_html=True)
                            st.caption(opts[k]["caption"])
                    with c2:
                        for k in ["ギャル", "王子"]:
                            st.markdown('<div class="planner-button">', unsafe_allow_html=True)
                            btn_lbl = f"旅好きインスタグラマー({k})" if k == "ギャル" else f"甘い言葉の{k}様"
                            is_selected = (selected_planner_name == opts[k]['name'])
                            button_type = "primary" if is_selected else "secondary"
                            if st.button(btn_lbl, key=f"pl_{k}", type=button_type):
                                st.session_state.planner = opts[k]
                                st.session_state.planner_selected = True
                                st.session_state.current_planning_stage = 2
                                planner_selected_in_stage = True
                            st.markdown('</div>', unsafe_allow_html=True)
                            st.caption(opts[k]["caption"])

                    if planner_selected_in_stage:
                        st.rerun()


                # --- ステージ 2: 基本情報入力 (ボタンUI, 状態維持確認) ---
                elif current_stage == 2:
                    st.subheader(f"ステップ {current_stage}/{total_stages}: 旅の基本情報を教えてください")

                    # 同行者
                    comp_options = ["一人旅", "夫婦・カップル", "友人", "家族"]
                    st.write("**👥 誰と行きますか？**")
                    cols_comp = st.columns(len(comp_options))
                    selected_comp_val = st.session_state.get('comp')
                    for i, opt in enumerate(comp_options):
                        with cols_comp[i]:
                            is_selected = (selected_comp_val == opt)
                            button_type = "primary" if is_selected else "secondary"
                            if opt in LONG_BUTTON_LABELS:
                                wrapper_class = "long-choice-button"
                            else:
                                wrapper_class = "choice-button"
                            st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
                            if st.button(opt, key=f"comp_btn_{opt}", type=button_type):
                                st.session_state.comp = opt
                                st.rerun()
                            st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown("---")

                    # 旅行日数
                    days_def = st.session_state.get('days')
                    days_val = days_def if isinstance(days_def, int) else 2
                    st.number_input("📅 何日間ですか？", min_value=1, max_value=30, step=1, value=days_val, key="days")
                    st.markdown("---")

                    st.text_input(
                        "🗾 希望の行き先都道府県はありますか？（任意）",
                        key="desired_destination", # このキーで入力値は session_state に一時的に保存される
                        value=st.session_state.get("desired_destination", ""), # 再描画時に入力値を維持
                        help="ここに入力された都道府県を行き先として優先します。空欄の場合は下の3つの質問からおすすめを選びます。"
                        )
                    st.markdown("---")

                    # 予算感
                    budg_options = ["気にしない", "安め", "普通", "高め"]
                    st.write("**💰 予算感は？**")
                    cols_budg = st.columns(len(budg_options))
                    selected_budg_val = st.session_state.get('budg')
                    for i, opt in enumerate(budg_options):
                        with cols_budg[i]:
                            is_selected = (selected_budg_val == opt)
                            button_type = "primary" if is_selected else "secondary"
                            if opt in LONG_BUTTON_LABELS:
                                wrapper_class = "long-choice-button"
                                print(f"DEBUG: Assigning '{wrapper_class}' to button '{opt}'")
                            else:
                                wrapper_class = "choice-button"
                            st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
                            if st.button(opt, key=f"comp_btn_{opt}", type=button_type):
                                st.session_state.budg = opt
                                st.rerun()
                            st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown("---")

                    # 次へ進むボタン
                    st.markdown('<div class="next-step-button-wrapper">', unsafe_allow_html=True)
                    st.markdown('<div class="next-step-button">', unsafe_allow_html=True)
                    if st.button("次へ進む", key="submit_basic_info"):
                        if not st.session_state.get('comp'): st.warning("同行者を選択してください。")
                        elif not st.session_state.get('budg'): st.warning("予算感を選択してください。")
                        else:
                            # ★★★★★ ここで 'desired_destination' の値を 'confirmed_destination' にコピー ★★★★★
                            current_destination_input = st.session_state.get('desired_destination', '').strip()
                            st.session_state['confirmed_destination'] = current_destination_input
                            print(f"DEBUG Stage 2 END: confirmed_destination に '{current_destination_input}' を保存")
                            st.session_state.current_planning_stage = 3
                            st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

                # --- ステージ 3: 行き先決定のための3問 ---
                elif current_stage == 3:
                    st.subheader(f"ステップ {current_stage}/{total_stages}: おすすめの行き先を見つけるために、いくつか質問です")

                    # Q1: 海/山
                    q0_options = ["海", "山", "どちらでも"]
                    st.write("**🌊 海と山、どっち派？**")
                    cols_q0 = st.columns(len(q0_options))
                    selected_q0_val = st.session_state.get('q0_sea_mountain')
                    for i, opt in enumerate(q0_options):
                        with cols_q0[i]:
                            is_selected = (selected_q0_val == opt)
                            button_type = "primary" if is_selected else "secondary"
                            st.markdown('<div class="choice-button">', unsafe_allow_html=True)
                            if st.button(opt, key=f"q0_btn_{opt}", type=button_type):
                                st.session_state.q0_sea_mountain = opt
                                st.rerun()
                            st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown("---")

                    # Q2: スタイル
                    q1_options = ["アクティブに観光", "ゆったり過ごす"]
                    st.write("**🏃 旅のスタイルは？**")
                    cols_q1 = st.columns(len(q1_options))
                    selected_q1_val = st.session_state.get('q1_style')
                    for i, opt in enumerate(q1_options):
                        with cols_q1[i]:
                            is_selected = (selected_q1_val == opt)
                            button_type = "primary" if is_selected else "secondary"
                            st.markdown('<div class="choice-button">', unsafe_allow_html=True)
                            if st.button(opt, key=f"q1_btn_{opt}", type=button_type):
                                st.session_state.q1_style = opt
                                st.rerun()
                            st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown("---")

                    # Q3: 雰囲気
                    q2_options = ["和の雰囲気", "モダン・都会的", "こだわらない"]
                    st.write("**🌸 どんな雰囲気を感じたい？**")
                    cols_q2 = st.columns(len(q2_options))
                    selected_q2_val = st.session_state.get('q2_atmosphere')
                    for i, opt in enumerate(q2_options):
                        with cols_q2[i]:
                            is_selected = (selected_q2_val == opt)
                            button_type = "primary" if is_selected else "secondary"
                            st.markdown('<div class="choice-button">', unsafe_allow_html=True)
                            if st.button(opt, key=f"q2_btn_{opt}", type=button_type):
                                st.session_state.q2_atmosphere = opt
                                st.rerun()
                            st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown("---")

                    # 次へ進むボタン
                    st.markdown('<div class="next-step-button-wrapper">', unsafe_allow_html=True)
                    st.markdown('<div class="next-step-button">', unsafe_allow_html=True)
                    if st.button("次へ進む", key="submit_destination_questions"):
                        if not st.session_state.get('q0_sea_mountain'): st.warning("「海と山、どっち派？」を選択してください。")
                        elif not st.session_state.get('q1_style'): st.warning("「旅のスタイルは？」を選択してください。")
                        elif not st.session_state.get('q2_atmosphere'): st.warning("「どんな雰囲気を感じたい？」を選択してください。")
                        else:
                            st.session_state.current_planning_stage = 4
                            st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)


                # --- ステージ 4: その他の好み入力 & 生成 (st.form を使用、radio は標準) ---
                elif current_stage == 4:
                    st.subheader(f"ステップ {current_stage}/{total_stages}: もっと詳しく好みを教えてください")
                    with st.form("preferences_form"):
                        st.markdown("**旅の好みについて**")

                        # スライダー (以下、フォーム内のウィジェットは変更なし)
                        # ... (スライダー、ラジオボタン、マルチセレクトなどの定義) ...
                        cols_slider = st.columns(4)
                        with cols_slider[0]: st.slider("🌲 自然", 1, 5, st.session_state.get('pref_nature', 3), key='pref_nature')
                        with cols_slider[1]: st.slider("🏯 歴史文化", 1, 5, st.session_state.get('pref_culture', 3), key='pref_culture')
                        with cols_slider[2]: st.slider("🎨 アート", 1, 5, st.session_state.get('pref_art', 3), key='pref_art')
                        with cols_slider[3]: st.slider("♨️ ウェルネス", 1, 5, st.session_state.get('pref_welness', 3), key='pref_welness')
                        st.markdown("---")
                        # 食事場所スタイル (st.radio)
                        food_loc_opts = ["地元の人気店", "隠れ家的なお店", "シェフのこだわりのお店", "オーガニック・ヴィーガン対応のお店"]
                        food_loc_def = st.session_state.get('pref_food_local', food_loc_opts[0])
                        try: food_loc_idx = food_loc_opts.index(food_loc_def) if food_loc_def in food_loc_opts else 0
                        except ValueError: food_loc_idx = 0
                        st.radio("🍽️ 食事場所スタイル", food_loc_opts, index=food_loc_idx, key='pref_food_local', horizontal=True)
                        st.markdown("---")
                        # 好きな料理・ジャンル
                        food_style_opts = ["和食", "洋食", "カフェ", "スイーツ", "郷土料理", "エスニック", "中華", "イタリアン"]
                        food_style_def = st.session_state.get('pref_food_style', [])
                        valid_food_style_val = [v for v in food_style_def if v in food_style_opts]
                        st.multiselect("🍲 好きな料理・ジャンル", food_style_opts, default=valid_food_style_val, key="pref_food_style")
                        st.markdown("---")
                        # 宿タイプ (st.radio)
                        accom_opts = ["ホテル", "旅館", "民宿・ゲストハウス", "こだわらない"]
                        accom_def = st.session_state.get('pref_accom_type', accom_opts[0])
                        try: accom_idx = accom_opts.index(accom_def) if accom_def in accom_opts else 0
                        except ValueError: accom_idx = 0
                        st.radio("🏨 宿タイプ", accom_opts, index=accom_idx, key='pref_accom_type', horizontal=True)
                        st.markdown("---")
                        # 気になるワード
                        word_opts = ["隠れた発見", "カラフル", "静かで落ち着いた", "冒険", "定番", "温泉", "寺社仏閣", "食べ歩き","ショッピング","日本酒","ワイン", "おこもり","子供と楽しむ", "ローカル体験", "アウトドア","写真映え", "パワースポット"]
                        word_def = st.session_state.get('pref_word', [])
                        valid_word_val = [v for v in word_def if v in word_opts]
                        st.multiselect("✨ 気になるワード (複数選択可)", word_opts, default=valid_word_val, key="pref_word")
                        st.markdown("---")
                        # MBTI
                        st.text_input("🧠 あなたのMBTIは？（任意：例 ENFP）", value=st.session_state.get("mbti", ""), key="mbti", help="性格タイプに合わせて提案が変わるかも？")
                        st.markdown("---")
                        # 画像アップロード
                        st.markdown("**🖼️ 画像からインスピレーションを得る (任意)**")
                        st.file_uploader("画像を3枚までアップロード", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="uploaded_image_files")
                        if st.session_state.uploaded_image_files and len(st.session_state.uploaded_image_files) > 3:
                            st.warning("画像は3枚まで。最初の3枚を使用します。")
                            st.session_state.uploaded_image_files = st.session_state.uploaded_image_files[:3]
                        st.markdown("---")
                        # 自由記述
                        st.text_area("📝 その他、プランナーへの要望があればどうぞ！", value=st.session_state.get("free_request", ""), key="free_request")


                        # 生成ボタン
                        st.markdown('<div class="generate-button-wrapper">', unsafe_allow_html=True)
                        st.markdown('<div class="generate-button">', unsafe_allow_html=True)
                        submitted_prefs = st.form_submit_button("好みを確定して旅のしおりを生成✨")
                        st.markdown('</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

                        if submitted_prefs:
                            with st.spinner(f"{st.session_state.planner['name']}が、{st.session_state.nickname}さんのためのしおりを作成中..."):
                                try:
                                    # --- ▼▼▼ 行き先決定ロジック修正 ▼▼▼ ---
                                    dest_int: Optional[str] = None
                                    print(f"DEBUG: Initial dest_int = {dest_int}")

                                    # 1. ユーザー入力のチェック
                                    user_input_raw: str = st.session_state.get("confirmed_destination", "").strip()
                                    print(f"DEBUG: confirmed_destination = '{user_input_raw}'")

                                    if user_input_raw:
                                        normalized_user = normalize_pref_name(user_input_raw)
                                        print(f"DEBUG: Normalized user input = '{normalized_user}'")
                                        match_pref = None
                                        for pref in st.session_state.all_prefectures:
                                            normalized_pref = normalize_pref_name(pref)
                                            if normalized_pref == normalized_user:
                                                match_pref = pref
                                                break
                                        print(f"DEBUG: Matched prefecture = {match_pref}")

                                        if match_pref:
                                            dest_int = match_pref
                                            print(f"DEBUG: User input matched. dest_int set to: {dest_int}")
                                            print(f"行き先決定（ユーザー指定）: {dest_int}")
                                        else:
                                            print("DEBUG: User input did not match any prefecture.")
                                            st.warning(f"入力された都道府県『{user_input_raw}』は認識できませんでした。質問回答をもとに提案します。")
                                            # dest_int remains None

                                    # 2. 質問ベースで決定 (ユーザー指定で決まらなかった場合のみ)
                                    print(f"DEBUG: Before checking 'if dest_int is None'. Current dest_int = {dest_int}")
                                    if dest_int is None:
                                        print("DEBUG: Entering 'if dest_int is None' block (This means user input was empty or invalid)")
                                        print("ユーザー指定の行き先がないか無効のため、質問ベースで決定します。")
                                        q_keys_dest = ["q0_sea_mountain", "q1_style", "q2_atmosphere"]
                                        map_prefs: Dict[str, Dict[str, List[str]]] = {
                                            "q0_sea_mountain": {
                                                "海": ["茨城県", "千葉県", "神奈川県", "静岡県", "愛知県", "三重県", "徳島県", "香川県", "高知県", "福岡県", "佐賀県", "沖縄県"],
                                                "山": ["山形県", "栃木県", "群馬県", "山梨県", "長野県", "岐阜県", "滋賀県", "奈良県"],
                                                "どちらでも": ["秋田県", "宮城県", "岩手県", "青森県", "北海道", "福島県", "福井県", "石川県", "富山県", "新潟県", "東京都","埼玉県","京都府","大阪府","兵庫県","和歌山県", "岡山県","鳥取県","島根県", "広島県", "山口県", "愛媛県", "大分県", "宮崎県", "鹿児島県", "長崎県", "熊本県"]
                                            },
                                            "q1_style": {
                                                "アクティブに観光": ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "大阪府", "兵庫県", "広島県", "福岡県", "熊本県"],
                                                "ゆったり過ごす": ["山梨県", "滋賀県", "京都府", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "佐賀県", "長崎県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]
                                            },
                                            "q2_atmosphere": {
                                                "和の雰囲気": ["青森県", "岩手県", "秋田県", "山形県", "福島県", "栃木県", "群馬県", "新潟県", "富山県", "石川県", "福井県", "岐阜県", "三重県", "滋賀県", "京都府", "奈良県", "和歌山県", "鳥取県", "島根県", "山口県", "徳島県", "愛媛県", "佐賀県", "長崎県", "熊本県", "大分県", "鹿児島県", "岡山県",  "香川県", "高知県"],
                                                "モダン・都会的": ["北海道", "宮城県", "茨城県","山梨県","長野県","埼玉県", "千葉県", "東京都", "神奈川県", "静岡県", "愛知県", "大阪府", "兵庫県", "広島県", "福岡県","宮崎県","沖縄県"],
                                                "こだわらない": st.session_state.all_prefectures
                                            }
                                        }
                                        cands: set[str] = {normalize_pref_name(p) for p in st.session_state.all_prefectures}

                                        for qk in q_keys_dest:
                                            ans = st.session_state.get(qk)
                                            print(f"DEBUG: Question-based loop: qk={qk}, ans={ans}")
                                            if not ans: continue
                                            norm_set = {normalize_pref_name(p) for p in map_prefs[qk].get(ans, st.session_state.all_prefectures)}
                                            cands &= norm_set
                                            print(f"DEBUG: Candidates after {qk}: {cands}")

                                        if not cands:
                                            print("DEBUG: No candidates left based on questions. Resetting to all prefectures.")
                                            st.warning("条件に合致する都道府県が見つからなかったため、ランダムに選びます。")
                                            cands = {normalize_pref_name(p) for p in st.session_state.all_prefectures}

                                        dest_base = random.choice(list(cands))
                                        print(f"DEBUG: Randomly chosen base name: {dest_base}")
                                        dest_int = next(
                                            (p for p in st.session_state.all_prefectures if normalize_pref_name(p) == dest_base),
                                            dest_base + "県",
                                        )
                                        print(f"DEBUG: Question-based logic finished. dest_int set to: {dest_int}")
                                        print(f"行き先決定（質問ベース）: {dest_int}")
                                    else:
                                        print("DEBUG: Skipped 'if dest_int is None' block because dest_int already has a value.")

                                    # 3. 最終的に決まった dest_int をセッションステートに保存 & プロンプト情報収集
                                    print(f"DEBUG: Final destination before saving to session state: {dest_int}")
                                    st.session_state.determined_destination_for_prompt = dest_int
                                    st.session_state.dest = dest_int

                                    prefs_prompt = {}
                                    for pk, sk in PREF_KEY_MAP.items():
                                        widget_key = sk
                                        q_def = next((q for q in question_definitions if q["key"] == sk), None)
                                        if q_def and q_def.get("key_suffix"): widget_key = f"{sk}{q_def['key_suffix']}"
                                        v = st.session_state.get(sk)
                                        if sk == "uploaded_image_files": v = st.session_state.get(widget_key)
                                        if v is not None and v != [] and v != "": prefs_prompt[pk] = v

                                    prefs_prompt['行き先'] = dest_int
                                    st.session_state.preferences_for_prompt = prefs_prompt
                                    print(f"Prefs for prompt:\n{json.dumps(prefs_prompt, indent=2, ensure_ascii=False)}")

                                    # プロンプト作成
                                    if not st.session_state.planner: st.error("プランナー未選択"); st.stop()
                                    nav_pers = st.session_state.planner.get("prompt_persona", "プロ旅行プランナーとして")
                                    days = st.session_state.get("days", 1)
                                    nickname_prompt = f"ユーザー（ニックネーム: {st.session_state.nickname}）"
                                    food_list = prefs_prompt.get('料理ジャンル', []); food_ex = food_list[0] if food_list else "食事"
                                    word_list = prefs_prompt.get('気になるワード', []); word_ex = word_list[0] if word_list else '観光'
                                    prompt = f"""
あなたは旅のプランナー「Okosy」です。{nickname_prompt}の入力情報をもとに、SNS映えや定番から少し離れた、ユーザー自身の感性に寄り添うような、パーソナルな旅のしおりを作成してください。
**ユーザーに最高の旅体験をデザインすることを最優先としてください。**
**【重要】ユーザーは具体的で最新の場所情報を求めています。そのため、以下の指示に従って必ず `search_google_places` ツールを使用してください。**

【基本情報】
- 行き先: {dest_int}
- 旅行日数: {days}日

【ユーザーの好み・要望】
{json.dumps(prefs_prompt, ensure_ascii=False, indent=2)}
★★★ 上記の好み（特に「自然」「歴史文化」「アート」「ウェルネス」の度合い、「気になるワード」、「MBTI（もしあれば）」、「自由記述」）や、ユーザーがアップロードした好みの画像（もしあれば、画像ラベルとして後述）も考慮して、雰囲気や場所選びの参考にしてください。{st.session_state.nickname}さんのための特別なプランを考えてください。 ★★★

【出力指示】
1. **構成:** 冒頭に、{st.session_state.planner['name']}として、{st.session_state.nickname}さんへの呼びかけから始め、なぜこの目的地({dest_int})を選んだのか、どんな旅になりそうか、全体の総括を **{nav_pers}** 言葉で語ってください。その後、{days}日間の旅程を、各日ごとに「午前」「午後」「夜」のセクションに分けて提案してください。時間的な流れが自然になるようにプランを組んでください。

2.  **内容:**
    * なぜその場所や過ごし方が{st.session_state.nickname}さんの好みに合っているか、**{nav_pers}言葉**で理由や提案コメントを添えてください。「気になるワード」や「自由記述」の要望を意識的にプランに盛り込んでください。MBTIタイプも性格傾向を考慮するヒントにしてください。画像から読み取れた特徴も踏まえてください。
    * 隠れ家/定番のバランスはユーザーの好みに合わせてください。
    * 食事や宿泊の好みも反映してください。
    * **【説明の詳細度】** 各場所や体験について、情景が目に浮かぶような、**{nav_pers}として感情豊かに、魅力的で詳細な説明**を心がけてください。単なるリストアップではなく、そこで感じられるであろう雰囲気や感情、おすすめのポイントなどを描写してください。{st.session_state.nickname}さんの好みを反映した説明をお願いします。

3. **【場所検索の実行 - 必須】** 以下の4種類の場所について、それぞれ **必ず `search_google_places` ツールを呼び出して** 最新の情報を取得してください。取得した情報は行程提案に **必ず** 反映させる必要があります。
    * **① 昼食:** `place_type`を 'restaurant' または 'cafe' として、ユーザーの好みに合う昼食場所を検索してください。（クエリ例: "{dest_int} ランチ {prefs_prompt.get('気になるワード', ['おしゃれ'])[0]}"）**ツール呼び出しを実行してください。**
    * **② 夕食:** `place_type`を 'restaurant' として、ユーザーの好みに合う夕食場所を検索してください。（クエリ例: "{dest_int} ディナー {food_ex} 人気"）**ツール呼び出しを実行してください。**
    * **③ 宿泊:** `place_type`を 'lodging' として、ユーザーの宿泊タイプや好みに合う宿泊施設を検索してください。（クエリ例: "{dest_int} {prefs_prompt.get('宿タイプ','宿')} {prefs_prompt.get('気になるワード', ['温泉', '静か'])[0]}"）**ツール呼び出しを実行してください。**
    * **④ 観光地:** `place_type`を 'tourist_attraction', 'museum', 'park', 'art_gallery' 等からユーザーの好みに合うものを選択し、関連する観光スポットを検索してください。（クエリ例: "{dest_int} {word_ex} スポット"）**ツール呼び出しを実行してください。**

4.  **【検索結果の利用と表示 - Google Mapsリンク】**
    * `search_google_places` ツールで得られた場所を提案に含める際は、その場所名に **Google Mapsへの検索リンク** を **Markdown形式** で付与してください。
    * **リンクのURL形式:** `https://www.google.com/maps/search/?api=1&query=Google&query_place_id=<PLACE_ID>` とし、`<PLACE_ID>` はツールの結果に含まれる `place_id` を使用してください。
    * **表示形式:** `[場所名](<上記のURL形式>)` のように、**場所名を角括弧で囲み、URLを丸括弧で囲んでください。**
    * **【最重要】** このMarkdownリンク (`[場所名](URL)`) **以外に、場所名をテキストとして記載しないでください。** リンクテキストがそのまま場所名として表示されるようにしてください。
    * デバッグ表示用のExpander（お店候補の表示）に出力する場所情報についても、上記と同じ形式のMarkdownリンクで場所名を表示するようにしてください。
    * **各日の夜のパートには、ステップ③のツール検索結果から**、**必ず**最適な宿泊施設を1つ選び、その名前と上記形式のGoogle Mapsリンクを記載してください。検索結果がない場合や検索しなかった場合でも、一般的な宿泊エリアやタイプの提案をしてください。
    * 初日は必ず午前から始め、ホテル情報は夕食後か夜のパートで提案してください。最終日は夜の情報を出力せず、午後で帰路につくようなプランにしてください。
    * ツール検索でエラーが出たり、場所が見つからなかったりした場合は、無理に場所名を記載せず、その旨を行程中に記載してください（例：「おすすめのレストラン（検索エラー）」「近くのカフェなど」）。

5.  **形式:** 全体を読みやすい**Markdown形式**で出力してください。各日の区切り（例: `--- 1日目 ---`）、午前/午後/夜のセクション（例: `**午前:**`）などを明確にしてください。

{st.session_state.planner['name']}として、{st.session_state.nickname}さんに最高の旅体験をデザインしてください。
"""
                                    st.session_state.messages_for_prompt = [{"role": "user", "content": prompt}]

                                     # API呼び出し
                                    final_res, places_res_json = run_conversation_with_function_calling(st.session_state.messages_for_prompt, st.session_state.get("uploaded_image_files", []))

                                     # 結果表示
                                    if final_res and "申し訳ありません" not in final_res and "エラー" not in final_res:
                                         st.session_state.itinerary_generated = True
                                         st.session_state.generated_shiori_content = final_res
                                         st.session_state.final_places_data = places_res_json
                                         st.success("しおり完成！"); st.balloons(); st.rerun()
                                    else:
                                         st.error("しおり生成中にエラーが発生しました。")
                                         print(f"AI Response Error or Failure: {final_res}")
                                         if final_res: st.error(f"AIからの応答: {final_res}")
                                         st.session_state.itinerary_generated = False
                                except Exception as gen_e:
                                     st.error(f"しおり生成中に予期せぬエラーが発生しました: {gen_e}")
                                     print(traceback.format_exc()); st.session_state.itinerary_generated = False

                # --- ステージが範囲外の場合 ---
                elif current_stage > total_stages:
                    st.warning("予期せぬ状態です。最初のステップに戻ります。")
                    st.session_state.current_planning_stage = 1
                    st.session_state.defaults_loaded = False
                    st.rerun()

    # --- 過去の旅のしおりを見る ---
    elif menu_choice == "過去の旅のしおりを見る":
        st.header("過去の旅のしおり")
        if not user_id: st.error("ユーザー情報未取得"); st.stop()
        itins = load_itineraries_from_firestore(user_id)
        if not itins: st.info("保存されたしおりはありません。")
        else:
            st.write(f"{len(itins)}件のしおりがあります。")
            itin_opts = {}
            for i in itins:
                name = i.get('name', '名称未設定'); date_str = "日付不明"; cdt = i.get('creation_date')
                if isinstance(cdt, datetime.datetime):
                    if cdt.tzinfo: cdt_jst = cdt.astimezone(datetime.timezone(datetime.timedelta(hours=9))); date_str = cdt_jst.strftime('%y/%m/%d %H:%M')
                    else: cdt_utc = cdt.replace(tzinfo=datetime.timezone.utc); cdt_jst = cdt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=9))); date_str = cdt_jst.strftime('%y/%m/%d %H:%M') + " (JST)"
                elif cdt: date_str = str(cdt)
                itin_opts[i['id']] = f"{name} ({date_str})"

            sel_id = st.selectbox("表示/編集/削除したいしおりを選択してください", [None] + list(itin_opts.keys()), format_func=lambda x: itin_opts.get(x, "--- 選択してください ---"), index=0, key="sel_itin_id_sel")
            st.session_state.selected_itinerary_id = sel_id

            if st.session_state.selected_itinerary_id:
                sel_itin = next((i for i in itins if i["id"] == st.session_state.selected_itinerary_id), None)
                if sel_itin:
                    st.subheader(f"しおり: {sel_itin.get('name', '名称未設定')}")
                    saved_nickname = sel_itin.get('nickname')
                    if saved_nickname: st.caption(f"ニックネーム: {saved_nickname}")
                    cdt_utc = sel_itin.get('creation_date')
                    if cdt_utc and isinstance(cdt_utc, datetime.datetime):
                         if cdt_utc.tzinfo: cdt_loc = cdt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=9))); st.caption(f"作成日時: {cdt_loc.strftime('%Y-%m-%d %H:%M')} JST")
                         else: cdt_assumed_utc = cdt_utc.replace(tzinfo=datetime.timezone.utc); cdt_loc = cdt_assumed_utc.astimezone(datetime.timezone(datetime.timedelta(hours=9))); st.caption(f"作成日時: {cdt_loc.strftime('%Y-%m-%d %H:%M')} JST")
                    elif cdt_utc: st.caption(f"作成日時: {str(cdt_utc)}")
                    else: st.caption("作成日時不明")

                    with st.expander("▼ このしおりを作成した時の好み", expanded=False):
                        prefs_d = sel_itin.get('preferences_dict', {})
                        if prefs_d: st.json(prefs_d)
                        else: st.info("保存された好み情報はありません。")

                    st.markdown(sel_itin.get("generated_content", "コンテンツがありません"))
                    st.markdown("---")

                    with st.expander("▼ 保存場所データ (デバッグ用)"):
                         data_str_past = sel_itin.get("places_data")
                         if data_str_past:
                             try:
                                 res_list_past = json.loads(data_str_past)
                                 titles_past = ["①昼食","②夕食","③宿泊","④観光"]
                                 if isinstance(res_list_past, list):
                                     for i, res_data_past in enumerate(res_list_past):
                                         title_past = titles_past[i] if i < len(titles_past) else f"Tool{i+1}"; st.subheader(title_past)
                                         places_past = None
                                         try:
                                             if isinstance(res_data_past, str): places_past = json.loads(res_data_past)
                                             elif isinstance(res_data_past, (list, dict)): places_past = res_data_past
                                             else: st.warning(f"不正形式:{type(res_data_past)}"); st.text(str(res_data_past)); continue
                                         except json.JSONDecodeError as json_e: st.error(f"JSONデコード失敗:{json_e}"); st.text(str(res_data_past)); continue
                                         except Exception as e: st.error(f"場所データ表示エラー:{e}"); st.text(str(res_data_past)); continue

                                         if places_past is not None:
                                             if isinstance(places_past, list):
                                                 if places_past:
                                                     try:
                                                         df_past = pd.DataFrame(places_past)
                                                         if 'place_id' in df_past.columns and 'name' in df_past.columns:
                                                             df_past['場所名(リンク付き)'] = df_past.apply(lambda r: f'<a href="https://www.google.com/maps/search/?api=1&query=Google&query_place_id={r["place_id"]}" target="_blank">{r["name"]}</a>' if pd.notna(r.get('place_id')) and r.get('name') else r.get('name',''), axis=1)
                                                             cols_to_display_past = ['場所名(リンク付き)', 'rating', 'address']
                                                         else:
                                                             st.warning("place_idまたはname欠損のためMapリンク不可")
                                                             cols_to_display_past = [col for col in ['name', 'rating', 'address'] if col in df_past.columns]
                                                             if 'name' in cols_to_display_past: df_past.rename(columns={'name': '場所名(リンク付き)'}, inplace=True); cols_to_display_past[cols_to_display_past.index('name')] = '場所名(リンク付き)'
                                                         df_disp_past = df_past[[c for c in cols_to_display_past if c in df_past.columns]].copy()
                                                         if 'rating' in df_disp_past.columns: df_disp_past['rating'] = df_disp_past['rating'].apply(lambda x: f"{x:.1f}" if pd.notna(x) and isinstance(x, (int, float)) else x)
                                                         html_past = df_disp_past.to_html(escape=False, index=False, na_rep="-", justify="left")
                                                         st.markdown(html_past, unsafe_allow_html=True)
                                                     except Exception as df_e: st.error(f"DF表示エラー:{df_e}"); st.json(places_past)
                                                 else: st.info("場所データ空")
                                             elif isinstance(places_past, dict):
                                                 if "error" in places_past: st.error(f"エラー:{places_past['error']}")
                                                 elif "message" in places_past: st.info(places_past['message'])
                                                 else: st.json(places_past)
                                             else: st.warning(f"不正データ形式:{type(places_past)}"); st.text(str(places_past))
                                 else: st.warning("場所データ形式不正(リストでない)"); st.text(data_str_past)
                             except json.JSONDecodeError: st.error("場所データ全体JSONデコード失敗"); st.text(data_str_past)
                             except Exception as e: st.error(f"場所データ処理エラー:{e}"); st.text(data_str_past)
                         else: st.info("保存された場所データはありません。")
                    st.markdown("---")

                   # 思い出投稿フォーム
                    st.subheader("✈️ 旅の思い出を追加")
                    if sel_itin and 'id' in sel_itin:
                        with st.form(f"mem_form_{sel_itin['id']}", clear_on_submit=True):
                            # ↓↓↓ ラベルを追加または確認 ↓↓↓
                            mem_cap = st.text_area("キャプション", key=f"mem_cap_{sel_itin['id']}") # ラベルあり OK
                            mem_pho = st.file_uploader("写真(任意)", type=["jpg","jpeg","png"], key=f"mem_pho_{sel_itin['id']}") # ラベルあり OK
                            submit_mem = st.form_submit_button("思い出を投稿する")
                            if submit_mem:
                                if mem_cap or mem_pho:
                                    pho_b64 = None
                                    if mem_pho:
                                        try: img_b = mem_pho.getvalue(); pho_b64 = base64.b64encode(img_b).decode('utf-8')
                                        except Exception as img_e: st.warning(f"写真処理エラー:{img_e}")
                                    saved_mid = save_memory_to_firestore(user_id, sel_itin['id'], mem_cap, pho_b64)
                                    if saved_mid: st.success("思い出を投稿しました！"); st.rerun()
                                    else: st.error("思い出の投稿に失敗しました。")
                                else: st.warning("キャプションまたは写真を入力してください。")
                    else: st.warning("しおりが選択されていません。")
                    st.markdown("---")

                    st.subheader("📖 思い出アルバム")
                    if sel_itin and 'id' in sel_itin:
                        mems = load_memories_from_firestore(user_id, sel_itin['id'])
                        if not mems: st.info("この旅の思い出はまだありません。")
                        else:
                            cols = st.columns(3); col_idx = 0
                            for mem in mems:
                                with cols[col_idx % 3]:
                                    st.markdown(f"**{mem.get('caption', '(キャプション無し)')}**")
                                    mcdt_utc = mem.get('creation_date')
                                    if mcdt_utc and isinstance(mcdt_utc, datetime.datetime):
                                        if mcdt_utc.tzinfo: mcdt_loc = mcdt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=9))); st.caption(f"{mcdt_loc.strftime('%y/%m/%d %H:%M')}")
                                        else: mcdt_assumed_utc = mcdt_utc.replace(tzinfo=datetime.timezone.utc); mcdt_loc = mcdt_assumed_utc.astimezone(datetime.timezone(datetime.timedelta(hours=9))); st.caption(f"{mcdt_loc.strftime('%y/%m/%d %H:%M')} JST")
                                    pho_img_obj = mem.get('photo_image')
                                    if pho_img_obj:
                                        try: st.image(pho_img_obj, use_column_width=True)
                                        except Exception as display_e: st.warning(f"画像表示エラー: {display_e}")
                                    mem_id_to_delete = mem.get('id')
                                    if mem_id_to_delete:
                                         if st.button("削除", key=f"del_mem_{mem_id_to_delete}", help="この思い出を削除します"):
                                             if delete_memory_from_firestore(user_id, sel_itin['id'], mem_id_to_delete): st.success("思い出を削除しました"); st.rerun()
                                             else: st.error("思い出の削除に失敗しました")
                                    st.markdown("---")
                                col_idx += 1
                    else: st.warning("しおりが選択されていません。")
                    st.markdown("---")

                    if sel_itin and 'id' in sel_itin:
                        st.error("⚠️ このしおりを削除する")
                        if st.button("削除を実行する (元に戻せません)", key=f"del_itin_{sel_itin['id']}", type="secondary", help="このしおりと、関連する全ての思い出が削除されます。"):
                            if delete_itinerary_from_firestore(user_id, sel_itin['id']):
                                st.success(f"しおり「{sel_itin.get('name','名称未設定')}」を削除しました")
                                st.session_state.selected_itinerary_id = None
                                if 'sel_itin_id_sel' in st.session_state: st.session_state.sel_itin_id_sel = None
                                st.rerun()
                            else: st.error("しおりの削除に失敗しました")

# --- フッター ---
st.sidebar.markdown("---")
st.sidebar.info("Okosy v1.7.3 (遷移修正適用)")