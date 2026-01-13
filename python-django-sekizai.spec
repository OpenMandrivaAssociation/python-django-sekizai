%define	module	django-sekizai
%define	oname	django_sekizai

Name:		python-django-sekizai
Summary:	Django Template Blocks with extra functionality
Version:	4.1.0
Release:	1
License:	BSD
Group:		Development/Python
URL:		https://github.com/ojii/django-sekizai/
Source0:	https://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(django) >= 3.2
BuildRequires:	python%{pyver}dist(django-classy-tags) >= 3
BuildRequires:	python%{pyver}dist(pre-commit)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Sekizai is media (css/js) framework for Django and Django CMS.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/sekizai
%{python_sitelib}/%{oname}-%{version}*.*-info
