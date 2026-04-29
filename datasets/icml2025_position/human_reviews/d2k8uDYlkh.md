## Human Reviewer 1

### Questions
- What concrete benchmarks (reporting FP32 vs FP64) could be used?
- Could you elaborate more on collaboration with natural scientists?

### Rating
3

### Confidence
4

---

## Human Reviewer 2

### Questions
1)  The paper argues for the use of FP64 in scientific ML, but what are the potential computational costs associated with this? Could the authors provide more details on how these costs might be mitigated (e.g., through mixed-precision training)?

### Rating
3

### Confidence
2

---

## Human Reviewer 3

### Questions
In the Alternative View section, what about adding the position "I can always transform my problem such that, even though there are numbers in my problem that are high precision, the ML method is only working on small differences that are themselves low in precision. That is, any high-precision problem can be transformed by scalings (for units) and subtractions (of high precision base expectations) into a low-precision problem" ? Maybe the best argument against this alternative view is the idea of integration of, say, differential equations over many steps, and finite-difference schemes?

[Note added in rebuttal period: raising Significance score by 1]

### Rating
3

### Confidence
4

---

## Human Reviewer 4

### Questions
- More details around the setup for non-ML and ML experiments are needed (such as hyperparameters and such). The authors directly jump into the discussion of results.
- In the non-ML section, it might be good to also provide some examples around where precision doesn't matter as much, to help paint a more complete picture.
- Fig 4, "though broader testing needed", what does this mean? Either remove or elaborate this statement.
- "model trained entirely in FP32 from the outset might behave differently", quite handwavy, why not just check. This handwavy explanation is not in line with other more clear arguments that the authors make elsewhere, and is reducing the quality of their argumentation.
- Lines 323-325, "For example", it is quite difficult to parse the sentence, would be good to rephrase.
- "specialized FD method", acronym not introduced before usage.
- "Most ML research has primarily explored lower-precision formats", this does seem to be a true statement, but nevertheless a reference should be provided.
- One of the bigger downsides of the paper is that the authors do not explore what are the downsides of their proposal, and the negative impact. E.g., for higher precision there would be more latency and costs to training and running the models, and so on. There should be some discussion around that to make the paper more complete.

Typos:
- Line 161, the whitespace are strangely written. The authors should check the text throughout the paper to clean up such minor issues.
- "which an open-source"
- Line 220, "10'6", what is meant here?
- "retrosynethsis"

### Rating
3

### Confidence
4