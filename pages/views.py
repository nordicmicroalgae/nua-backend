from django.http import JsonResponse

# Dummy view for testing purposes
def get_page(request, page_slug):
    available_pages = [
        'introduction',
        'latest-images',
        'hall-of-fame',
        'how-to-contribute',
        'partners',
        'nomp',
        'helcom-peg',
        'links',
        'literature'
    ]

    if not page_slug in available_pages:
        return JsonResponse({'message': 'Page not found'}, status=404)

    return JsonResponse({
        'page': {
            'title': page_slug,
            'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, '
                  + 'sed do eiusmod tempor incididunt ut labore et dolore '
                  + 'magna aliqua. Ut enim ad minim veniam, quis nostrud '
                  + 'exercitation ullamco laboris nisi ut aliquip ex ea '
                  + 'commodo consequat. Duis aute irure dolor in reprehenderit '
                  + 'in voluptate velit esse cillum dolore eu fugiat nulla '
                  + 'pariatur. Excepteur sint occaecat cupidatat non proident, '
                  + 'sunt in culpa qui officia deserunt mollit anim id est '
                  + 'laborum.'
        }
    })
