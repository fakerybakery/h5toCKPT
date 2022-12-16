curl "https://raw.githubusercontent.com/fakerybakery/.shell/main/shell/banner/banner.txt"
echo "Welcome to mrfakename's H5 to CKPT converter!"
echo "Installing packages..."
pip3 install -r requirements.txt
echo "Starting server..."
python3 main.py
