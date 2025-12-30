def welcome():
  print("Hii your welcome")

print(__name__)
if __name__ == "__main__":
 welcome()


  # Now, because narendra.py is being imported,
  # __name__ will NOT be "__main__" — it will be the module name "narendra".
  # But since __name__ == "narendra" (not "__main__"),
  # ❌ This block will NOT run.

  # So welcome() is not called yet.