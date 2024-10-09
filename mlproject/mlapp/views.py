from django.shortcuts import render
import joblib
import numpy as np
from django.views.decorators.csrf import csrf_exempt  # นำเข้าตัวตกแต่ง csrf_exempt
from .forms import PredictionForm

# โหลดโมเดลที่บันทึกไว้
model = joblib.load('mlapp/models/best_lgb_model.pkl')

@csrf_exempt  # ปิดการตรวจสอบ CSRF
def predict(request):
    prediction = None
    result = None  # ตัวแปรสำหรับเก็บผลการทำนาย
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # ดึงข้อมูลจากฟอร์มและแปลงเป็นตัวเลข
            age = int(form.cleaned_data['age'])
            gender = int(form.cleaned_data['gender'])
            tenure = int(form.cleaned_data['tenure'])
            usage_frequency = int(form.cleaned_data['usage_frequency'])
            support_calls = int(form.cleaned_data['support_calls'])
            payment_delay = int(form.cleaned_data['payment_delay'])
            subscription_type = int(form.cleaned_data['subscription_type'])
            contract_length = int(form.cleaned_data['contract_length'])
            total_spend = float(form.cleaned_data['total_spend'])
            last_interaction = int(form.cleaned_data['last_interaction'])
            
            # สร้างข้อมูลในรูปแบบที่โมเดลต้องการ
            features = np.array([[age, gender, tenure, usage_frequency, support_calls, payment_delay,
                                  subscription_type, contract_length, total_spend, last_interaction]])
            
            # ทำนายผล
            prediction = model.predict(features)[0]
            
            # แสดงผลการทำนาย
            result = "ลูกค้าเลิกใช้งาน" if prediction == 1 else "ลูกค้าไม่เลิกใช้งาน"
    else:
        form = PredictionForm()

    return render(request, 'mlapp/index.html', {'form': form, 'prediction': result})
