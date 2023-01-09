from reader.compressed import bzipped,gzipped

extension_map = {
  '.bz2':bzipped.opener,
  '.gz2':gzipped.opener
}
class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(self.filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
