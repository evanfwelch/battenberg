from pygit2 import Repository, discover_repository, init_repository


__commit_init_message__ = 'Initialized repository'


def open_repository(path):
    return Repository(discover_repository(path))


def open_or_init_repository(path):
    try:
        return open_repository(path)
    except Exception:
        # Not found any repo, let's make one.
        pass

    repo = init_repository(path)
    repo.create_commit(
        'HEAD',
        repo.default_signature, repo.default_signature,
        __commit_init_message__,
        repo.index.write_tree(),
        []
    )
    return repo
