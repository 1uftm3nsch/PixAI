# PixAI - AI Critique-Guided Image Editor

Dự án đồ án: Ứng dụng web chỉnh sửa ảnh thông minh thông qua phản biện ngôn ngữ tự nhiên (AI Critique).

---

## 📁 Cấu trúc dự án

```text
PixAI/
├── docs/                   # Tài liệu đặc tả, DB schema, API contract, báo cáo
├── frontend/               # Next.js 14+ App Router, Tailwind CSS (Full-Stack)
├── backend/                # Python FastAPI, Multimodal LLM & Diffusion API (AI Engine)
├── scripts/                # Scripts test, benchmark, seed dữ liệu
├── docker-compose.yml      # Chạy thử nghiệm đồng bộ qua Docker
└── README.md               # Hướng dẫn dự án
```

---

## 🚀 Hướng dẫn khởi chạy

### 1. Backend (FastAPI)
```bash
cd backend
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
# source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```
Swagger UI tài liệu API: `http://localhost:8000/docs`

### 2. Frontend (Next.js)
```bash
cd frontend
npm install # hoặc pnpm install
cp .env.example .env.local
npm run dev
```
Truy cập web tại: `http://localhost:3000`

---

## 👥 Phân công nhiệm vụ (Nhóm 1 - 2 thành viên)
- **Thành viên A (Full-Stack):** Phụ trách thư mục `frontend/`, Supabase Auth & Storage, Canvas, Before/After Slider.
- **Thành viên B (AI Engineer):** Phụ trách thư mục `backend/`, Gemini Parser, Inpainting Pipeline, Auto-critique.

