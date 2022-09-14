# External Import
from itertools import chain

# Django Core Import
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Internal import
from .forms import TicketForm, ReviewForm, FollowUsersForm, ReviewExistingTicketForm
from .models import Ticket, Review


@login_required
def home(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()

    context = {
        "tickets": tickets,
        "reviews": reviews,
    }
    return render(request, "appreview/home.html", context=context)


@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('appreview:home')
    else:
        form = TicketForm()

    context = {
        "form": form,
    }
    return render(request, "appreview/create-ticket.html", context=context)


@login_required
def create_review_existing_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        review_form = ReviewExistingTicketForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket_id = ticket.pk
            review.user = request.user
            review.save()
            return redirect('appreview:home')
    else:
        review_form = ReviewExistingTicketForm()

    context = {
        "ticket": ticket,
        "review_form": review_form,
    }
    return render(request, "appreview/create-review-existing-ticket.html",
                  context=context)


@login_required
def create_review(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket_id = ticket.id
            review.user = request.user
            review.save()
            return redirect('appreview:home')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }
    return render(request, "appreview/create-review.html", context=context)


@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = TicketForm(instance=ticket)
    if request.method == "POST":
        edit_form = TicketForm(request.POST, instance=ticket)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("appreview:my_posts")

    context = {
        "edit_form": edit_form,
    }
    return render(request, "appreview/update-ticket.html", context=context)


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        ticket.delete()
        return redirect("appreview:my_posts")
    context = {
        "ticket": ticket,
    }
    return render(request, "appreview/delete-ticket.html", context=context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        review.delete()
        return redirect("appreview:my_posts")
    context = {
        "review": review,
    }
    return render(request, "appreview/delete-review.html", context=context)


@login_required
def review_update(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    edit_form = ReviewForm(instance=review)
    if request.method == "POST":
        edit_form = ReviewForm(request.POST, instance=review)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("appreview:my_posts")

    context = {
        "edit_form": edit_form,
    }
    return render(request, "appreview/update-review.html", context=context)


@login_required
def my_posts(request):
    tickets = Ticket.objects.filter(user_id=request.user)
    reviews = Review.objects.filter(user_id=request.user)
    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda instance:
    instance.time_created, reverse=True)

    context = {
        "tickets": tickets,
        "reviews": reviews,
        "tickets_and_reviews": tickets_and_reviews,
    }
    return render(request, "appreview/my_posts.html", context=context)


@login_required
def followers(request):
    form = FollowUsersForm(instance=request.user)

    context = {
        "form": form,
    }
    return render(request, "appreview/followers.html", context=context)
