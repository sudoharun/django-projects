from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Consultation
from .forms import CreateConsultationForm

def create_consultation(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    if request.method == 'GET':
        form = CreateConsultationForm(user=request.user)
    else:
        form = CreateConsultationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created consultation!')
            return redirect('user_consultations')

    return render(request, 'create_consultation.html', {'form': form})

def edit_consultation(request, consultation_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    consultation = get_object_or_404(Consultation, pk=consultation_id)

    if request.method == 'GET':
        form = CreateConsultationForm(instance=consultation)
    else:
        form = CreateConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.user = request.user
            consultation.save()

            messages.success(request, f'Successfully edited consultation #{consultation.id}!')
            return redirect('user_consultations')

    return render(request, 'edit_consultation.html', {'form': form})

def delete_consultation(request, consultation_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to access this page!')
        return redirect('home')

    consultation = get_object_or_404(Consultation, pk=consultation_id)
    consultation.delete()
    messages.success(request, 'Successfully deleted the consultation!')
    return redirect('user_consultations')
