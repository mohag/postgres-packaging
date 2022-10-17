%global sname   percona-ppg-server-ha
%global pgmajorversion 14
%global version 4

Summary:        Percona selection of PostgreSQL%{pgmajorversion} HA components
Name:           %{sname}%{pgmajorversion}
Version:        %{version}
Release:        1%{?dist}
License:        PostgreSQL
Group:          Applications/Databases
URL:            https://www.percona.com/software/postgresql-distribution
Packager:       Percona Development Team <https://jira.percona.com>
Vendor:         Percona, LLC
BuildArch:      noarch

Requires:       etcd
Requires:       percona-patroni
Requires:       percona-haproxy

%description
Essential / key PostgreSQL14 high availability components
Percona Distribution for PostgreSQL features core components, tools and add-ons
from the community, tested to work together in demanding enterprise environments

%files

%changelog
* Mon Aug 08 2022 Kai Wagner <kai.wagner@percona.com> 15.0-1
- Initial build
