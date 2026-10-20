import qrcode

# আপনার GitHub বা Google Drive এর লিংক বা ডকুমেন্ট ডিটেইলস এখানে বসাবেন
data_link = "আপনার_লিংক_বা_ডকুমেন্ট_ডিটেইলস_এখানে_দিন"

# কিউআর কোড জেনারেট করার সেটিংস
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=2,
)

qr.add_data(data_link)
qr.make(fit=True)

# কিউআর কোড ইমেজ তৈরি এবং সেভ করা
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_new_qr.png")

print("QR Code generated successfully!")
