# -*- coding: utf-8 -*-
from flask import Flask, render_template, abort, request, redirect, url_for, flash

from . import content as C


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mcg-replica-dev-key"

    services_by_slug = {s["slug"]: s for s in C.SERVICES}
    insights_by_slug = {i["slug"]: i for i in C.INSIGHTS}

    # Make common data available to every template.
    @app.context_processor
    def inject_globals():
        return {
            "site": C.SITE,
            "nav": C.NAV,
            "services": C.SERVICES,
        }

    @app.route("/")
    def home():
        return render_template(
            "home.html",
            home=C.HOME,
            services=C.SERVICES,
            insights=C.INSIGHTS,
            expertise=C.EXPERTISE,
            partners=C.PARTNERS,
        )

    @app.route("/services/<slug>")
    def service(slug):
        svc = services_by_slug.get(slug)
        if not svc:
            abort(404)
        return render_template("service.html", svc=svc)

    @app.route("/our-expertise")
    def our_expertise():
        return render_template(
            "expertise.html", expertise=C.EXPERTISE, intro=C.HOME["expertise_intro"]
        )

    @app.route("/case-studies")
    def case_studies():
        return render_template("case_studies.html", cases=C.CASE_STUDIES)

    @app.route("/our-team")
    def our_team():
        return render_template("team.html", team=C.TEAM)

    @app.route("/featured-insights")
    def featured_insights():
        return render_template("insights.html", insights=C.INSIGHTS)

    @app.route("/featured-insights/<slug>")
    def insight(slug):
        art = insights_by_slug.get(slug)
        if not art:
            abort(404)
        return render_template("insight.html", art=art)

    @app.route("/mcg-arabia")
    def mcg_arabia():
        return render_template("arabia.html")

    @app.route("/contact-us", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            # In a real deployment this would email or persist the enquiry.
            name = (request.form.get("name") or "").strip()
            flash(
                "Thank you%s. Your enquiry has been received \u2014 we'll be in touch shortly."
                % ((", " + name) if name else ""),
                "success",
            )
            return redirect(url_for("contact"))
        return render_template("contact.html")

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5055)
