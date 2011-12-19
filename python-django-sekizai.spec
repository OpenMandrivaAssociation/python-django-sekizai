%define	module	django-sekizai
%define name	python-%{module}
%define version	0.4.2
%define release %mkrel 1

Summary:	Media framework for Django
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/ojii/django-sekizai/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-django-classy-tags >= 0.3.1
BuildRequires:	python-django-classy-tags >= 0.3.1
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx

%description
Sekizai is media (css/js) framework for Django and Django CMS.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
make html
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc LICENSE README.rst docs/_build/html
