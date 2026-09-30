from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.certification import Certification
from app.schemas.certification import CertificationCreate


class CertificationService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_certifications(self) -> list[Certification]:
        stmt = select(Certification).order_by(Certification.issue_date.desc())
        return self.db.scalars(stmt).all()

    def create_certification(
        self,
        certification_data: CertificationCreate,
    ) -> Certification:
        certification = Certification(
            name=certification_data.name,
            issuer=certification_data.issuer,
            issue_date=certification_data.issue_date,
            credential_url=certification_data.credential_url,
            description=certification_data.description,
        )

        self.db.add(certification)
        self.db.commit()
        self.db.refresh(certification)

        return certification