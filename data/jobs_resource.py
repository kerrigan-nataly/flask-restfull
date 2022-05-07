from flask import jsonify
from flask_restful import Resource, abort

from data import db_session
from data.jobs import Jobs
from data.jobs_parser import parser


def abort_if_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(
            only=('id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'team_leader', 'is_finished'))})

    def delete(self, job_id):
        abort_if_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id', 'job', 'work_size', 'user.name', 'collaborators', 'start_date', 'end_date', 'is_finished')
        ) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            job=args['job'],
            work_size=args['work_size'],
            team_leader=args['team_leader'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            end_date=args['end_date'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK', 'job_id': job.id})
