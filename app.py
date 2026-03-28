from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove
import io

app = FastAPI()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    # इमेज को पढ़ना
    input_image = await file.read()
    
    # बैकग्राउंड हटाना
    output_image = remove(input_image)
    
    # परिणाम को वापस भेजना
    return Response(content=output_image, media_type="image/png")
  
