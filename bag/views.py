from django.shortcuts import render


def view_bag(request):
    """ a view to render the bag contents """

    return render(request, 'bag/bag.html')