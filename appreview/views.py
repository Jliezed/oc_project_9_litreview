# External Import
from itertools import chain

# Django Core Import
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.db import IntegrityError

# Internal import
from .forms import TicketForm, ReviewForm, FollowUsersForm
from .models import Ticket, Review, UserFollows


@login_required
def home(request):
    user_obj = UserFollows.objects.filter(user__exact=request.user)
    user_following = user_obj.values("followed_user_id")

    tickets = Ticket.objects.filter(
        Q(user__in=user_following) | Q(user__exact=request.user))
    reviews = Review.objects.filter(
        Q(user__in=user_following) | Q(user__exact=request.user))
    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda instance:
    instance.time_created, reverse=True)

    context = {
        "tickets": tickets,
        "reviews": reviews,
        "tickets_and_reviews": tickets_and_reviews,
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
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket_id = ticket.pk
            review.user = request.user
            review.save()
            return redirect('appreview:home')
    else:
        review_form = ReviewForm()

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
        print(request.POST)
        print(request.COOKIES)
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
        "review": review,
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
    # Get User information
    users_following = UserFollows.objects.filter(user_id=request.user)
    users_followed_by = UserFollows.objects.filter(followed_user=request.user)

    error_msg = ""
    if request.method == "POST":
        form = FollowUsersForm(request.POST)

        try:
            if form.is_valid():
                user = form.save(commit=False)
                user.user = request.user
                user.save()
                return redirect('appreview:followers')
        except ObjectDoesNotExist:
            error_msg = "L'utilisateur n'existe pas"
        except IntegrityError:
            error_msg = "Vous ??tes d??j?? abonn?? ?? cet utilisateur"

    else:
        form = FollowUsersForm(request.POST)

    context = {
        "form": form,
        "users_following": users_following,
        "users_followed_by": users_followed_by,
        "error_msg": error_msg,

    }
    return render(request, "appreview/followers.html", context=context)


@login_required
def unfollow(request, user_id):
    user = get_object_or_404(UserFollows, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("appreview:followers")
    context = {
        "user": user,
    }
    return render(request, "appreview/unfollow.html", context=context)