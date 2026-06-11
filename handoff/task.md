Your task input:
results/2026_deepseek_train_balanced

Your task output:
A hf dataset for ZTO.

1. for each review sample in the 2026_deepseek_train_balanced, use embedding search (using gemini embedding, look at `code/main.py`) to find 10 similar reviews in the 10 score bins in the dataset (datasets/deepreview_13k_calibration, the database embedding is cached, look at the main.py for detail), exlucde itself.
2. Now for each review, you have 10 anchor, make them into 10 pairs, the given review is always the first one and the anchor is always second one. Remove scores and decisions from all reviews. 
3. Make it into an openai query, with system message briefly saying you need to determine whcih review's paper is better (not the review itself) the first one is AI generated and the second one (anchor) is human written. AI could soemtimes be too nice. This wil yield a messages list of [system, review1+review2]. The expected output should be a single number 0/1. 0 means the first one is better. 
4. collect all pairs, it should have 10xN pairs. Send each of them for 3 times to deepseek-v4-flash API via openrouter (look main.py for detail), turn reasoning on with high effort, collect the reasoning content and final answer, make it as a sample. if the answer is correct, make it as positive sample of ZTO, if wrong, make it as negative sample of ZTO. The right/wrong should be a simple comparsion with the anchor GT (in the csv) and the GT of the input review.

Do a test on this pipeline, if it works, run the whole thing with 300 reviews (not the whole 2026_deepseek_train_balanced)