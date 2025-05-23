from unitxt import add_to_catalog
from unitxt.metrics import RelaxedCorrectness
from unitxt.test_utils.metrics import test_metric

metric = RelaxedCorrectness(n_resamples=None)

predictions = ["10", "30"]
references = [["14"], ["30"]]

# how to create a metric which isn't updated in every sample when using UNITXT?
instance_targets = [
    {
        "relaxed_overall": 0.0,
        "relaxed_human_split": 0.0,
        "score": 0.0,
        "score_name": "relaxed_overall",
    },
    {
        "relaxed_overall": 1.0,
        "relaxed_augmented_split": 1.0,
        "score": 1.0,
        "score_name": "relaxed_overall",
    },
]

global_target = {
    "relaxed_overall": 0.5,
    "relaxed_human_split": 0.0,
    "relaxed_augmented_split": 1.0,
    "score": 0.5,
    "score_name": "relaxed_overall",
    "num_of_instances": 2,
}
outputs = test_metric(
    metric=metric,
    predictions=predictions,
    references=references,
    instance_targets=instance_targets,
    global_target=global_target,
    task_data=[{"type": "human_test"}, {"type": "augmented_test"}],
)
add_to_catalog(metric, "metrics.relaxed_correctness", overwrite=True)
