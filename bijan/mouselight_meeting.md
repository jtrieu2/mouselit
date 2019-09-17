project based in the miller lab

hopkins focused on image side of things, and how to process

we have 1 complete cleared mouse brain, 30tb
you can open it in the janelia workstation
    highlight and annotate where the neurons are
    save annotations in "fragment files".
    we have a big dump of fragment files (generated automatically)
    
the "guys" have an rf-based pipeline with a LOT of false positives
they did human-based annotations to connect

v1: they connect all the fragments
v2: they generally redo everything from scratch

we have 1-2 layers of human-annotated stuff (ground truth)

even if we wanted to, we are not well-trained proofreaders so its a bad idea to manually do anything.

we are trying to get their annotations on wednesday.

creating smaller fragment pieces
connecting fragments afterwards (another deep net)

3 years project, first year we only receive a little data ("toy")
later on we would expand to a huge scale.

we do not have labeled data at the moment.
the group is visiting janelia on wednesday

a little bit of noise (background differences) to get rid of with preprocessing. one region will be slightly darker/brighter than another.

meeting to talk to janelia ppl about their preprocessing.

they used a naive RF (guess, nobody knows).

they are doing the union of all the labeled neurons across different mouse brains that all got registered. we are avoiding the question of multiple of the same, since there are so many more neurons than the labeled ones we have.

generating fragments requires inhomogeneity correction

metric between fragments whether they are in the same axon, connecting

no guarantee on data within the first 3 months.
are we allowed to use this as a course-based project? have to ask the main PIs. Drs Miller and Mueller, and Janelia. Doubtful.
Maybe also have to ask natascha.

publishing in the future is maybe really touchy. how to arrange authorship etc.
