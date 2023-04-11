#Routes
#------
def test_index_success(client):
  # Page loads
  response = client.get('/')
  assert response.status_code == 200
  
def test_about_success(client):
  # Page loads
  response = client.get('/about')
  assert response.status_code == 200
    
def test_legal_success(client):
  # Page loads
  response = client.get('/legal')
  assert response.status_code == 200
  
  
def test_cookies_index_success(client):
  # Page loads
  response = client.get('/cookies')
  assert response.status_code == 200    
   
def test_route_fail(client):
   # Page dose not exist
   response = client.get('/bla')
   assert response.status_code == 404
   
#Page Content   
#------------
def test_index_content(client):
  # Returns Download link
  response = client.get('/')
  assert b'Download legal details' in response.data
  
  
#Headers
#-------
def test_legal_download(client):
  # Returns legal.txt file
  response = client.get('/legal')
  assert response.headers['Content-Disposition'] == 'attachment; filename=legal.txt'