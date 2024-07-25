from django.http import JsonResponse
from django.db import connection

def get_lot_by_id(request, idlot):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Client WHERE ClientID = %s", [idlot])
        row = cursor.fetchone()

    if row:
        response_data = {
            'idlot': row[0],
            # Ajoutez les autres champs ici, par exemple :
             'nom': row[5],
             'email': row[2],
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Lot not found'}, status=404)
