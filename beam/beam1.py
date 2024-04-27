import apache_beam as beam

def split(element):
  if element:
    return element.split(",")
  else:
    return []


def capital(element):
  if element:
    element[1]=element[1].capitalize()
    return element
  else:
    return []

with beam.Pipeline() as p:
  (
      p
      |'read data' >> beam.io.ReadFromText('dept_data.txt')
      |'transform data' >> beam.Map(split)
      |'remove data' >> beam.Map(lambda x: x[:-1])
      |'name in upper case' >> beam.Map(capital)
      |'write data' >> beam.io.WriteToText('data/output')
)
