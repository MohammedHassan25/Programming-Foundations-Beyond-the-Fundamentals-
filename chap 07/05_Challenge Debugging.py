# def plant_recommendation(care):
#     if care = 'low':
#         print('aloe')
#     elif care == 'medium':
#         print('pothos')
#     elif care == 'medium':
#         print('orchid')


# plant_rec('low')
# plant_recommendation('medium')
# plant_recommendation('high')

# The solution
def plant_recommendation(care):
    if care == 'low':         # Not (care = 'low')
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':       # Not (care == 'medium')
        print('orchid')


plant_recommendation('low')         # Not (plant_rec('low'))
plant_recommendation('medium')
plant_recommendation('high')
