from app.core.schema import *

def test_constraint_creation():

    constraint = Constraint(
        constraint_id="c1",
        constraint="Budget < $500",
        constraint_type=ConstraintType.HARD,
        priority=1.0,
        status=ConstraintStatus.ACTIVE,
        confidence=0.9,
    )

    assert constraint.constraint_id == "c1"
    assert constraint.constraint_type == ConstraintType.HARD
    assert constraint.status == ConstraintStatus.ACTIVE


def test_query_creation():

    query = Query(
        query="Find flights"
    )

    assert query.query == "Find flights"

def test_extractor_output():

    output = ExtractorOutput[dict](
        run_id="123",

        extracted_constraints=[
            Constraint(
                constraint_id="c1",
                constraint="Budget < $500",
                constraint_type=ConstraintType.HARD,
                status=ConstraintStatus.ACTIVE,
            )
        ],

        extracted_queries=[
            Query(
                query="Flights NYC LA"
            )
        ],

        extracted_data={
            "budget": 500
        }
    )

    assert output.run_id == "123"

    assert len(
        output.extracted_constraints
    ) == 1

    assert len(
        output.extracted_queries
    ) == 1

    assert output.extracted_data[
        "budget"
    ] == 500


def test_input_schema():

    input_obj = Input(
        run_id="123",

        input="Tokyo itinerary",

        domain=Domain.TRAVEL
    )

    assert (
        input_obj.domain
        == Domain.TRAVEL
    )

def test_global_state_creation():

    state = GlobalState(

        run_id="123",

        domain=Domain.TRAVEL,

        input=Input(
            run_id="123",
            input="Tokyo trip"
        )
    )

    assert state.run_id == "123"

    assert state.domain == Domain.TRAVEL

    assert state.current_status == (
        AgentRunningState.ACTIVE
    )

    assert len(state.history) == 0


def test_candidate_creation():

    candidate = Candidate(

        candidate_id="poi_1",

        candidate_type="poi",

        name="Tokyo Tower"
    )

    assert (
        candidate.name
        == "Tokyo Tower"
    )

def test_cluster_creation():

    cluster = ClusterOutput(
        cluster_id="c1",
        name="Shibuya"
    )

    assert cluster.cluster_id == "c1"

def test_anchor_creation():

    anchor = AnchorOutput(
        anchor_id="a1",
        candidate_id="c1.1",
        cluster_id="c1",
        name="Shibuya Crossing"
    )

    assert (
        anchor.cluster_id
        == "c1"
    )

def test_global_state_serialization():

    state = GlobalState(
        run_id="123",

        domain=Domain.TRAVEL,

        input=Input(
            run_id="123",
            input="Tokyo"
        )
    )

    payload = state.model_dump()

    assert payload["run_id"] == "123"