## Human Reviewer 1

### Questions
To follow up on my comment above, I would like to ask how we can prevent "moving the goal post"?

### Rating
5

### Confidence
4

---

## Human Reviewer 2

### Questions
1. L220: "...an evaluation should be considered leaked the moment it has been shared online or sent over the wire. Adopting this rule of thumb significantly improves our ability to trust the results of evaluations and gives them substantially more robustness." It isn't clear what "robustness" precisely means. Could the authors present a detailed clarification?
2. L341: "...secure backend without access to internet. By evaluating all models securely offline, competitions platforms can guarantee no hidden test data is leaked." What about proprietary models? How might they fit in with this paradigm?
3. In Fig. 2, two views are presented in the top and bottom panels. Though I understand the contrast that the authors intend to provide, is it not the case that parallel submissions to conferences/ArXiv convert the top panel into the bottom panel? If that is indeed the case, then I do not see much difference between the proposal and the existing state of evaluations.

### Rating
3

### Confidence
3

---

## Human Reviewer 3

### Questions
1. My main question to the authors is how they would define "AI Competition" (see W1). Depending on this definition, some of my weaknesses might not apply as written above (or could change).
2. Do you have any evidence that competition rankings correlate with real-world performance more than static leaderboards?
3. You argue that "meta-analyses should be valued as highly in the field of AI as they are in fields such as medicine". I like this point, but it is quite short on details in the paper. Could you elaborate a bit more, e.g. what meta-analyses could look like in our field, especially when using AI Competitions?

I also have a few additional questions and comments. However, they don't fall under the category of "the response would likely change my opinion" and are thus not critical to the review process. I am still interested in the authors' response, though, or think the feedback could be helpful to strengthen the paper.

4. On a very high level, I would be interested in the authors' thoughts on how much of the GenAI evaluation issues have to do with the fact that we allow full control over the training set. I.e. in traditional ML benchmarks, $D_{train}$ was fixed (i.e. we wanted to see results on an ImageNet validation set, if trained only on the ImageNet training set). Do you think that GenAI evaluations would profit from this lens? For example, a competitive leaderboard of LLM model architecture that fixes aspects like the training set, training protocol, etc.
5. Do you think that novelty-based generalization could simply be a different task than iid generalization in the sense that both have their place but we should be transparent about which of those we are currently measuring?
6. There are a few (potential) minor typos in the paper. For example:
   - Line 34 (right): "rigorous and robust evaluation [of?] GenAI models..."
   - The use of title case for headings is inconsistent. E.g. "1.2 Structure of this paper" vs. "2.1 The Rise of Reproducible Benchmarks".
   - I think some of the citations should be text citations (e.g. \citet or \textcite) instead of bracketed citations. For example, in line 143 (left) "As authors, we were deeply surprised by the work of Roelofs et al. (2019b)".
   - Line 318 (right): Double "the" in "the the".
   - Line 318 (right): I am not familiar with the word "writ" as it is used in this sentence. Perhaps replacing it with "at" would improve readability?

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Questions
1. The main method of creating leak-proof competition structure involves evaluating the model based on data that does not exist at the training time. Would that be a clearer summary organizing the paragraphs?
2. The authors mentioned that for reproducible benchmarks, overfitting was not the main issue. Are there more explanations why it was not the main issue?

### Rating
4

### Confidence
4