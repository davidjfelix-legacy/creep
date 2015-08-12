import uuid
from json import JSONDecodeError
import tornado.ioloop
import tornado.web
import tornado.escape

class CategoryHandler(tornado.web.RequestHandler):

    def delete(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                self.write(ghetto_db['categories'].pop(card_id))
            else:
                self.set_status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'DELETE not allowed without category id'})

        raise tornado.web.Finish()

    def get(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                self.write(ghetto_db['categories'][card_id])
            else:
                self.set_status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(200)
            self.write(ghetto_db['categories'])

        raise tornado.web.Finish()

    def head(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode(ghetto_db['cateogies'][category_id]))
                )
            else:
                self.set_status(404)
                self.set_header('Content-Length',
                    len(tornado.escape.json_encode({'error': 'category id not found'}))
                )
        else:
            self.set_status(200)
            self.set_header('Content-Length',
                len(tornado.escape.json_encode(ghetto_db['cards']))
            )

        raise tornado.web.Finish()

    def options(self, category_id=None):
        global ghetto_db

        if category_id:
            if cateogry_id in ghetto_db['categories']:
                self.set_status(200)
                self.set_header('Accept', 'DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT')
            else:
                self.set_Status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(200)
            self.set_header('Accept', 'GET, HEAD, OPTIONS, POST')

        raise tornado.web.Finish()

    def patch(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                self.write("Patch goes here")
            else:
                self.set_status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'PATCH not allowed without card id'})

        raise tornado.web.Finish()

    def post(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(409)
                self.write({'error': 'category id already exists'})
            else:
                self.set_status(405)
                self.write({'error': 'POST not allowed with category id'})
        else:
            category_id = str(uuid.uuid4())
            while category_id in ghetto_db['categories']:
                category_id = str(uuid.uuid4())
            try:
                category = tornado.escape.json_decode(self.request.body)
            except JSONDecodeError:
                self.set_status(400)
                self.write({'error': 'Malformed JSON request'})
                raise tornado.web.Finish()
            self.set_status(201)
            ghetto_db['categories'][category_id] = category
            self.write({'id': category_id, 'content': category})

        raise tornado.web.Finish()

    def put(self, category_id=None):
        global ghetto_db

        if category_id:
            if category_id in ghetto_db['categories']:
                self.set_status(200)
                category = tornado.escape.json_decode(self.request.body)
                ghetto_db['categories'][category_id] = category
                self.write({'id': category_id, 'content': category})
            else:
                self.set_status(404)
                self.write({'error': 'category id not found'})
        else:
            self.set_status(405)
            self.write({'error': 'PUT not allowed without category id'})

        raise tornado.web.Finish()