    env:
        conda env update --file environment.yml --prune
        conda env create -n ligo -file environment.yml

    html:
        myst build --html

    clean:
        rm -rf figures/* audio/* _build/*