# Repository writing audit

Reviewed 25 October 2026. Review only: existing content has not been edited.

This assesses how the writing reads, not who wrote it. Priorities describe editorial impact, not a probability of AI authorship. The local `skill.md` informed the review; punctuation, technical vocabulary, and deliberate uncertainty are not treated as problems on their own.

## Issues found

### P0: Credibility checks before stylistic editing

These passages need author confirmation or supporting material. A smoother rewrite would not resolve them.

- `blog/otr-copilot/index.html:245` and `otr-copilot.html:245`: “Listeners reported ~65% improvement in interpretation accuracy”. The capstone PDF, page 51, describes approximately 65% pattern recognition accuracy, with a macro-averaged F1 methodology. These are different measurements. Confirm whether there is a separate source for the improvement claim; otherwise report the measured result with its limitations. The same paragraph calls the capability “irreplaceable” and says “no individual supporter” can perform it. Both overstate the small evaluation.
- `blog/otr-copilot/index.html:249` and `otr-copilot.html:249`: “The mechanism is RLHF-trained agreeableness”. The June update at line 103 also states this as the cause. The described observation is that Gemini mirrored avoidance despite instructions. That observation alone does not establish the training mechanism. Separate the observed behaviour from a proposed explanation. Example direction: “In these tests, Gemini mirrored the seeker's avoidance despite the empathy instructions. I suspect agreeableness contributed, but these tests did not isolate the cause.”
- `blog/half-moon-bay/index.html:45`: the surfer's direct quotation also becomes the essay's closing lesson. Confirm it is a remembered quotation. If it is an approximation, label it as such. The story's unusually convenient resolution makes accuracy especially important here; this is not a finding that the encounter was invented.
- `blog/not-yet-dead/index.html`: numerous direct quotations, numerical claims, and descriptions of Joseph Wong's speech underpin the argument. Check against notes or a transcript before republishing or rewriting. In particular, keep attributed speech distinct from the author's interpretation. No external fact-check was performed in this audit.

### P1: Strongest editorial targets

#### Half Moon Bay — high priority

`blog/half-moon-bay/index.html`

- Line 33, “Saltwater, Silicon, and Something Like Grace”: the alliterative triad and vague spiritual payoff prepackage the experience into a magazine-style lesson. A simpler title would let the scene do more work.
- Line 41, “Sometimes that's the gift you can give”: generic wisdom after a specific conversation. Cut the second sentence; “I mostly listened” already conveys it.
- Line 43, “the surrender of it—the Pacific's vastness, the cold shock, the comfort of company that doesn't need you to be anything”: stacked emotional abstractions. Keep the cold water and failed surfing; explain any emotional significance in the author's own concrete terms.
- Lines 52–60, “The whole apparatus of Silicon Valley” / “the real debugging happened in the water” / “The Pacific doesn't optimize. It just is.”: an extended tech-versus-humanity metaphor with a predictable aphorism. Retain only the observations that actually mattered to this outing. The ocean/optimization contrast is carrying too much of the essay.
- Lines 65–69, “showed up anyway” / “And somehow, that was enough”: stock reassurance closing an already resolved story. Ending on spending the day with Will would be stronger than adding another lesson.

Assessment: revise the reflective connective tissue substantially; preserve the actual day, friendship, and details. Adding slang to the existing structure would not address the issue.

#### Red Dot to Big Apple — high priority

`blog/red-dot-to-big-apple/index.html`

- Line 37, “the intimate version of the city that tourists rarely see”: familiar travel-writing exceptionalism. Start with staying with Arin or the particular shop interaction instead.
- Line 39, “construct an existence” / “You don't maintain friendships across oceans by accident”: inflated description followed by a ready-made maxim. The effort involved in maintaining this friendship is more interesting if there is an actual example to tell.
- Line 48, “authenticity matters less than audacity” / “a thesis statement about the place”: turns one chicken-rice visit into a claim about an entire city. Keep the meal and the reaction; narrow the inference.
- Lines 50–52, “the bigger beautiful mess” and the paragraph repeating “It doesn't ask”: broad romantic claims with little connection to the week described. Replace with an encounter that supports the feeling, if one exists; otherwise shorten.
- Line 56, “Brooklyn, where audacity meets authenticity”: generic slogan caption. Name the photographed place.
- Lines 61–65, “something electric still humming under my skin” / “permission to become someone you haven't been yet” / “I'm still learning”: three successive emotional endings. Pick the thought that actually follows from spending time with Arin, and stop there.

Assessment: one of the least distinctive voices in the repository. The friendship and meal supply a useful starting point, but the city-as-personal-transformation framing overwhelms them.

#### Hustle culture — high priority

`blog/hustle-culture-questions/index.html`

- Line 37, “Four incredible panelists” / “build meaningful lives without destroying themselves”: promotional praise and a sweeping opening. State who spoke and what the panel addressed.
- Lines 39–41, “wore busyness like a badge of honor” / “confusing motion with meaning”: familiar self-improvement language. Keep the actual measures of productivity if accurate; remove the slogans around them.
- Lines 48 and 58, “wasn't the answers ... it was the questions” / “The conversation that mattered most happened in the questions, not the answers”: repeats the same rhetorical contrast without adding an observation. Keep one plain explanation at most.
- Lines 63–71, “more questions than when I arrived” / “still sitting with them” / “I don't have clean conclusions” / “The questions continue”: four versions of an unresolved ending. The audience question about parents at line 61 is more specific and could carry the ending.
- Line 67, “the willingness to sit with these questions ... might be exactly what we need”: presents uncertainty itself as a reassuring answer. Say which question still affects the author, or cut.

Assessment: keep the panel and audience details. Reduce the repeated declarations of complexity and uncertainty.

#### Not Yet Dead — high priority, including structure

`blog/not-yet-dead/index.html`

- Lines 112–114, “refusing the categories that make marginalization legible” / “interrogating the systems”: abstract significance assigned to an otherwise vivid ice-cream outing. Explain what the group actually discussed rather than making the group symbolize the argument.
- Lines 118–124, “one phrase ... explains everything” / “Read it again slowly. Notice three things”: overpromising and reader instruction. Introduce the quotation and explain the relevant interpretation directly.
- Lines 227–231, “The single most important variable” / “You can't engineer trust. You can't optimize your way past historical trauma”: escalating absolutes followed by parallel slogans. Ground the point in the example and limit its scope.
- Lines 249–268, “The technology question” / “The human question” / “That came from listening, not engineering” / “We chose dignity”: several binaries turn a concrete language-interface finding into a moral victory. Keep the finding: workers wanted convenient mixed-language input and proper-script output.
- Lines 297–337, “Not charity. Not service delivery. Infrastructure” / “This is how democracies collapse”: dramatic fragments and a sweeping causal conclusion. Distinguish Wong's argument from the author's inference and reduce the scale of unsupported claims.
- Lines 455–465, “extractive research with better aesthetics” / “carrying the discomfort matters”: memorable phrasing substitutes for explaining the actual maintenance problem. The unfunded future of the chatbot is concrete enough to stand on its own.
- Lines 467–620: five lessons, another conference summary, an “Unfinished Question,” personal plans, and a final reprise all restate similar conclusions. Consolidate heavily. The ending “Building bridges between systems and humanity. Between ideas and impact” is particularly generic.
- Final refrain, “Joe lives ... Fully. With dignity, agency, dreams, and belonging. That's the standard”: a rhetorically complete ending after several earlier endings. Consider ending on Selvan's unanswered question about whether the tool will survive the research instead.

Assessment: the largest structural cleanup. Preserve specific findings, acknowledge the unresolved implementation problem once, and remove repeated manifestos. This page is absent from `blog/posts.json`, but its file still warrants review because it can be opened directly.

#### Determined — high priority

`determined.html`

- Line 57, “the quiet grief of being human”: vague literary subtitle that promises more than the review specifies.
- Lines 59–63, “hit me like a diagnosis I'd been avoiding” / “breathe meritocracy like humidity” / “a machine running code it didn't write”: three substantial metaphors in the opening. Choose the one that reflects the experience most accurately; state the rest plainly.
- Line 75, “And yet. There's something liberating in the wreckage”: staged emotional pivot. Explain what changed in the author's view of deservingness.
- Line 79, “What would I tell her now?”: confirm that the pronoun is intentional. It is an authorial-consistency check, not an authorship inference.
- Line 88, “won't give you answers” / “some people seem to glide while others grind”: familiar book-review conclusion and polished alliteration. End with the specific reservation about Sapolsky's treatment of philosophy or the effect on the author's own thinking.

### P2: Local edits and judgment calls

#### When the Solution Stopped Being the Point

`blog/solution-stopped-being-the-point/index.html`

- Line 55, “It produced something more uncomfortable: doubt”: overly staged pivot. The preceding scene already conveys hesitation.
- Lines 61–65, “Frameworks feel grounding” / “permission to think originally”: general interpretation around a strong concrete exchange with Dilip Soman. Keep the exchange and reduce the explanatory gloss.
- Line 75, “There was so much intelligence already in the room”: generic praise. The workers' existing financial knowledge is the substantive point; describe it if there is an example to add.
- Lines 94–102, repeated “Maybe,” “sitting with that discomfort,” and “infrastructure ... trust and solidarity”: the ending moves away from the actual design problem into the same abstract vocabulary used in other essays. The next paragraph about listening before intervening already supplies a sufficient conclusion.
- Line 115, “time, trust, and care” / “less like a project and more like a conversation”: formulaic gratitude language. Optional polish only; the named acknowledgements deserve to stay.

Assessment: substantially more grounded than the high-priority posts. Preserve the Toronto huddle, direct exchange, and specific doubts.

#### OTR Copilot, both copies

`blog/otr-copilot/index.html` and `otr-copilot.html` contain substantially duplicated prose. Apply any eventual editorial changes to both, or establish one canonical page.

- Line 117, “presence, not advice” / “heard, not fixed” / “No frameworks, no prescribed responses”: the role distinction is useful, but three formulations in succession feel rehearsed. Keep one clear explanation.
- Line 230, “Privacy was non-negotiable” / “support human work, not surveil it”: values slogans surround useful implementation details. Lead with data minimization and pseudonymization.
- Lines 238–246, “The Assistance Paradox” / “Longitudinal Intelligence” / “The design question this reframes”: grand labels and repeated reframing language. More direct headings would be “Suggestions interrupted conversations” and “Patterns across sessions.”
- Line 240, “cognitively burdensome” / “naturally separable”: academic abstractions obscure a clear finding about competing for attention during a conversation.
- Lines 264–266, three parallel “was about” explanations ending in “The AI suggests; the mentor decides”: reads like a prepared values statement. Keep the actual design reasons and avoid treating trust and accuracy as mutually exclusive.
- Line 269, “human flourishing ... ambient intelligence” / “emotional, economic, cognitive life”: broad philosophical framing exceeds the specificity of this capstone. Optional reduction; the coursework may be relevant, but the testing example explains the point more clearly.

Assessment: most of the build/test narrative is useful and concrete. Resolve the P0 claims before polishing its language.

#### Wicked Problems, HTML and Markdown draft

`blog/wicked-problems/index.html` and `blog/wicked-problems/wickedproblems.md`

- HTML line 42 and draft opening, “a check-in that also manifested itself in a form of accountability”: inflated phrasing. “It also made me feel accountable” is a possible direction, if accurate.
- HTML line 72 and draft, “In the literature there is a reference to a phenomenon known as Goodhart's Law”: textbook throat-clearing. Introduce the concept directly.
- HTML line 97 and draft, “building on the right foundation”: familiar metaphor after a more specific explanation of grant and computing-school incentives. Could be cut.
- HTML lines 124–130: the epilogue adds several versions of continuing to ask questions. Keep the research direction and consider shortening the final return to “questions.”
- Markdown closing, “something real, with genuine constraints ... a shifting landscape”: more generic than the revised HTML closing. If the draft is reused, carry over the plainer HTML version.

Assessment: mostly leave alone. The Graz exchange, grant constraints, late-night Slack messages, hesitations, and informal asides supply a recognizable voice. Typos are a separate copy-editing issue; preserving voice does not require preserving accidental errors.

#### I Was Wrong About Economics

`blog/wrong-about-economics/index.html`

- Line 53, “the capacity to see things the framework couldn't see”: abstract restatement. The following rational-actor discussion provides a more useful explanation.
- Lines 59–63, “perform certainty” / “I'm still sitting with”: familiar reflective phrasing, especially alongside other posts. Optional shortening rather than a full rewrite.
- Lines 69–71, “A bet that paid off. Not the only possible answer” / “I think the asking matters”: successive fragments package an unresolved reading response into a lesson. Ending on which assumptions need examining at work would be more specific, without inventing a conclusion.

Assessment: low-to-moderate priority. Its work context and particular reading experience carry the essay well.

#### Books and reading copy

`books.json` is generated by `books.py` from Goodreads RSS. Edit the source reviews for lasting changes; local JSON edits can be overwritten.

- Line 136, Determined: “got something closer to an autopsy” / “dismantles an entire moral economy” / “the mirror stops accusing and starts explaining”: stacked metaphors and aphorisms. Keep the London/Minh opening and the specific philosophical reservation.
- Line 144, A Journey in Ladakh: “the colors, smells, sounds ... come alive” / “you're not reading ... you're walking it” / “retains transformative power”: standard praise. The distinction between Taoist influence and Buddhist discipline is more distinctive. Leave the attributed anecdote untouched.
- Line 152, Dreams from My Father: “sitting with the discomfort is itself part of the work” and repeated “not ... but” constructions around law and community. Keep the Ipoh encounter and Mauritian connection; reduce the abstract conclusions.
- Line 160, Where I Was: “the questions it raises feel more valuable than any definitive answers”: repeats a repository-wide closing pattern. End with the concrete coalition-building tension instead.
- Line 176, Against Happiness: “the refusal to resolve it is his own subtle provocation”: tidy interpretation without enough explanation. Optional cut or expand with a specific passage from the book.
- Lines 200 and 208, The Third Door / Anything You Want: “Great read for any aspiring or budding entrepreneur” / “Must read for anyone”: generic endorsements. Say which idea was useful, if remembered; otherwise shorten.
- Line 223, What I Know for Sure: “illustrious look” / “bite-sized gold nuggets” / “a peek into her spiritual ways”: promotional review language. Replace with a plain description of what the author took from it.
- Lines 231, 239, and 255: “will tug the heart of any reader” / “Necessary reading for any SaaS entrepreneur” / “Truly inspiring”: universal praise with no supporting detail. Remove or replace with a personal, specific reaction.
- Line 192, Deep Work: “Actionable steps ... foster”: low priority. The actual reservation about app-heavy workplaces is clear; isolated vocabulary is not sufficient reason for a rewrite.
- `reading.html:119`, “Reviews reflect my personal thoughts and takeaways”: redundant boilerplate. The first sentence already describes the page.

Assessment: mixed. Many reviews have specific associations, doubts, and multilingual observations worth preserving. Lowercase, slang, and imperfect punctuation do not automatically make a passage sound personal, just as polished grammar does not make it sound generated.

#### Short public descriptions

- `blog/posts.json:126`, “Exploring ethical implications ... ethical design principles”: repeats “ethical” and mainly restates the title. Narrow to the questions the paper addresses; do not invent its findings.
- `blog/posts.json:136`, “A sociological exploration of artificial intelligence's transformative impact”: says almost nothing beyond the title. Replace with the paper's actual argument after reading it. This audit did not open the external paper.
- `blog.html:204`, “Personal reflections and lived experience”: generic category description. Optional; “Personal essays” would serve the same navigational purpose.
- `research.html:123`, “complex challenges affecting underserved communities” / “interdisciplinary and field-based”: institutional boilerplate. The next paragraph supplies more concrete project context. Shorten the consortium introduction if desired.

Assessment: the About and Research pages are generally clear. Keep the interest-rate example, language background, and actual research design. Technical phrases such as “mechanistic interpretability” are appropriate to the subject.

#### Repository documentation

- `.github/copilot-instructions.md`, final paragraph: “tell me which area to expand and I'll update this file.” Clear conversational assistant residue inside persistent documentation. Delete the invitation; it is not a repository instruction.
- `SETUP_CHECKLIST.md:156`, “You're almost there! ... beautifully showcased ... 🚀”: assistant-style congratulatory ending. Delete it.
- `SETUP_CHECKLIST.md:5–6` and commit-message example: “enhanced” / “comprehensive” repeatedly praise the work rather than describe it. Use factual change descriptions. Emoji headings are optional cleanup in a checklist, not a substantive writing problem.
- `assets/img/otr-copilot/README.md` and `assets/pdf/README.md`: procedural and mostly useful. No substantial voice cleanup needed. File paths, image dimensions, and checklists should remain concrete.
- `skill.md`: an instructional reference full of intentionally quoted AI-writing examples. Exclude those examples from findings against the site's voice. Its sweeping lexical rules should not be applied mechanically to personal essays or technical work.

#### Capstone PDF — limited text review

`assets/pdf/cis_capstone.pdf` has 63 pages. Extracted text was scanned, with closer review of selected opening, evaluation, and discussion passages. This is not a complete line edit of the report or a verification of its references.

- PDF page 52, “This section examines the implications ... interpreting results within the context”: unnecessary section narration. Start with the substantive finding about cognitive load.
- PDF page 52, “This aligns with but extends ...” / “exceptionally careful attention to preserving the natural flow of human interaction”: significance inflation and vague emphasis around a concrete workflow finding. Explain the actual contribution and observed disruption.
- PDF page 50, “strongly validated this hypothesis”: stronger than the small testing session alone appears to warrant. Review the claim against the study design; retain the participant feedback.
- Across the report, “comprehensive,” “seamless,” and related terms occur repeatedly. These are secondary flags only. Technical section structure and lists are appropriate in a capstone and do not need to be made conversational.

## Assessment and coverage

The primary issue is repetition of a rhetorical approach: a scene, a contrast between technology and humanity, an abstract realization, and an ending about unresolved questions. These ideas may be sincere, but repeated packaging makes otherwise different experiences sound interchangeable.

Suggested order: (1) resolve the OTR measurement and causal claims; (2) revise Half Moon Bay, Red Dot, and Hustle Culture; (3) consolidate Not Yet Dead; (4) trim repeated endings in the stronger essays; (5) remove documentation residue and generic review endorsements.

The best voice references are the concrete portions of Wicked Problems, the About page, the build-and-test sections of OTR, and the book reviews' specific memories and disagreements. Preserve uncertainty where it describes actual uncertainty. Prefer cutting generic reflections to manufacturing fresh anecdotes or adding slang.

Coverage includes the site's HTML prose, internal blog posts and templates, the Markdown draft, post metadata, book reviews, repository guides and instructions, and first-party code comments and UI strings. No material prose issues stood out in the helper scripts, workflows, redirect/fetch pages, or ordinary code comments. Dependency lockfiles, third-party code, Git internals, and binary media were not treated as authored prose. External Medium articles and linked papers were not reviewed. The poster PDF has no extractable text and remains unreviewed; image/video text was not transcribed. The capstone review is limited as described above.

Some posts discussed here are absent from the blog index; that lowers their visibility but does not remove them from the repository. Suggested directions are editorial options, not applied rewrites. No authorship score is assigned.
